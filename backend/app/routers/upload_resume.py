from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import json
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from core.logger import logger
from core.embedding import embedding
from database.database import SessionLocal
from models.resume import Resume
from models.analysis import Analysis
from services.ai_service import ask_llm
from utils.json_utils import clean_json_response
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from models.roles import Role
from uuid import uuid4

#  PASTE THIS LINE INSTEAD
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from pathlib import Path
import chromadb


router = APIRouter(
    tags=["Upload Resume"],
    
)

ALLOWED_EXTENSIONS = {".pdf"}

FILE_SAVE_PATH = r"C:\Users\gaura\OneDrive\Documents\ai-resume-analyzer\backend\upload"


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="chat_collection"
)

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):

    logger.info("Resume upload request received.")

    ext = os.path.splitext(file.filename)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        logger.warning(f"Invalid file type: {file.filename}")
        raise HTTPException(
            status_code=415,
            detail="Only PDF files are allowed."
        )

    contents = await file.read()

    save_path = os.path.join(FILE_SAVE_PATH, file.filename)

    with open(save_path, "wb") as f:
        f.write(contents)
        logger.info(f"Resume saved at: {save_path}")

    logger.info(f"Resume uploaded successfully: {file.filename}")

    reader = PdfReader(save_path)
    logger.info("Reading uploaded PDF.")

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        
        if page_text:
            text += page_text

    logger.info(f"Resume text extracted ({len(text)} characters).")

    db = SessionLocal()
    logger.info("Opening database session.")

    try:
        # ---------------------------
        # Save Resume
        # ---------------------------
        resume = Resume(
            file_name=file.filename,
            file_data=contents
        )
        
        logger.info("Saving resume to database.")
        db.add(resume)
        db.commit()
        
        db.refresh(resume)
        logger.info(f"Resume stored in database. Resume ID: {resume.id}")
        
        # ---------------------------
        # AI Analysis
        # ---------------------------
        logger.info("Sending resume to Qwen for analysis.")
        
        # selected_role = "Backend Developer"   # Temporar
    
        role_id = 5
        
        logger.info(f"Fetching role with ID: {role_id}")
        role = db.query(Role).filter(Role.role_id == role_id).first()
        if not role:
            logger.warning(f"Role not found for role_id={role_id}")
            raise HTTPException(status_code=404 , detail="Role Not Found")
        
        selected_role = role.role_name      
        logger.info(f"Role selected: {selected_role}")              
        BASE_DIR = Path(__file__).resolve().parent.parent
        KNOWLEDGE_DIR = BASE_DIR / "knowledge"
        
        
        knoweldge_file_path = KNOWLEDGE_DIR / role.knowledge_file
        
        print(knoweldge_file_path)
        print(knoweldge_file_path.exists())
                
        if not knoweldge_file_path.exists():
            logger.warning(f"Knowledge file not found: {knoweldge_file_path}")
            raise HTTPException(
                status_code=404, 
                detail=f"Knowledge file '{role.knowledge_file}' not found."
            )
            
            
        logger.info(f"Loading knowledge file: {knoweldge_file_path}")    
            
        reader1 = PdfReader(knoweldge_file_path)
        logger.info("Reading knowledge PDF.")        
        
        text1 = ""
        
        
        for i, page in enumerate(reader1.pages):
            logger.info(f"Reading knowledge PDF page {i + 1}")
            page_text = page.extract_text()
            
            logger.info(f"Resume contains {len(reader1.pages)} pages.")

            # print("Extracted:", page_text is not None)
            logger.info(f"Text extracted from page {i + 1}: {page_text is not None}")

            if page_text:
                text1 += page_text

        # print("Final Length:", len(text1))
        
        logger.info(f"Knowledge text extracted successfully. Total characters: {len(text1)}")
        
        
        text_splitter  = RecursiveCharacterTextSplitter(
            chunk_size = 100,
            chunk_overlap = 0
        )
        
        logger.info("Splitting knowledge into chunks.") 
        
               
        
        split_texts = text_splitter .split_text(text1)
        
        logger.info(f"Total chunks created: {len(split_texts)}")
        
        logger.info("Generating embeddings for knowledge chunks.")
        
        genrate_embedding = embedding(split_texts)
        logger.info("Knowledge embeddings generated successfully.")
        
        logger.info("Storing embeddings in ChromaDB.")        
        question_searching = collection.add(
                ids=[str(uuid4()) for _ in split_texts],
                documents=split_texts,
                embeddings=genrate_embedding,
                metadatas=[
                    {
                        "source": str(knoweldge_file_path),
                        "chunk": i
                    }
                    for i in range(len(split_texts))
                ]
            )

        logger.info("Knowledge stored in ChromaDB.")

        logger.info("Knowledge embeddings stored successfully in vector database.")
        
        logger.info("Generating resume embedding.")
        resume_embedding = embedding([text])[0]
        logger.info("Resume embedding generated successfully.")       
        logger.info("Searching relevant knowledge from ChromaDB.") 
        results = collection.query(
            query_embeddings= [resume_embedding],
            n_results=5
        )
        
        retrieved_docs = results["documents"][0]
        
        logger.info(f"Retrieved {len(retrieved_docs)} relevant knowledge chunks.")
        role_knowledge = "\n\n".join(retrieved_docs)
        logger.info("Knowledge retrieval completed successfully.")                
            
        logger.info("Sending prompt to Qwen LLM.")
        
        analysis = ask_llm(
            resume_text=text,
            selected_role=selected_role,
            role_knowledge=role_knowledge)
        
        
        analysis = clean_json_response(analysis)
        logger.info("LLM response cleaned successfully.")
        

        logger.info("AI analysis completed.")
        # print(repr(analysis))
        
        # logger.info(f"Qwen Response:\n{analysis}")
        import json

        # print("=" * 100)
        # print(json.dumps(analysis, indent=2))
        # print("=" * 100)
        # analysis = json.loads(analysis)

        # ---------------------------
        # Save Analysis
        # ---------------------------
        
        
        analysis_db = Analysis(
            resume_id=resume.id,
            ats_score=analysis["ats_score"],
            summary=analysis["summary"],
            technical_skills=", ".join(analysis["technical_skills"]),
            soft_skills=", ".join(analysis["soft_skills"]),
            # missing_skills=", ".join(analysis["missing_skills"]),
            missing_skills="\n".join(
    f"{item['skill']} ({item['priority']}) - {item['reason']}"
    for item in analysis["missing_skills"]
),
            # suggestions=", ".join(analysis["suggestions"]),
    #         suggestions="\n".join(
    # f"{item['title']} - {item['description']}"
    # for item in analysis["suggestions"]),         
            # learning_roadmap=analysis["learning_roadmap"],
            
            learning_roadmap="\n".join(
    f"Step {item['step']}: {item['title']} - {item['description']}"
    for item in analysis["learning_roadmap"]
),
            # suggested_projects=", ".join(analysis["suggested_projects"]),
            suggested_projects="\n".join(
    f"{item['title']} - {item['description']}"
    for item in analysis["suggested_projects"]
),
            # estimated_timeline=", ".join(analysis["estimated_timeline"]),
            estimated_timeline=analysis["estimated_timeline"],
            action_plan=", ".join(analysis["action_plan"]),
#             action_plan="\n".join(
#     f"{item['title']} - {item['description']}"
#     for item in analysis["action_plan"]
# ),
            
            ## gamma 
            
        suggestions="\n".join(
    f"{item['title']} - {item['description']}"
    for item in analysis["suggestions"]
),    
        )
        
        logger.info("Saving analysis to database.")

        db.add(analysis_db)
        db.commit()
        db.refresh(analysis_db)
        
        
        resume_id = resume.id
        analysis_id = analysis_db.id

        logger.info(
            f"Analysis stored in database. Analysis ID: {analysis_db.id}"
        )
    
    except Exception as e:
        logger.error(
        f"Error while processing resume: {str(e)}",
        exc_info=True
    )
        raise

    finally:
        logger.info("Closing database session.")
        db.close()    

    return {
    "message": "Resume uploaded and analyzed successfully.",
    "resume_id": resume_id,
    "analysis_id": analysis_id,
    "technical_skills":analysis["technical_skills"],
    "summary":analysis["summary"],
    "missing_skills":analysis["missing_skills"],
    "suggestions":analysis["suggestions"],
    "ats_score":analysis["ats_score"],
    "soft_skills":analysis["soft_skills"],
    "learning_roadmap":analysis["learning_roadmap"],
    "suggested_projects":analysis["suggested_projects"],
    "estimated_timeline":analysis["estimated_timeline"],
    "action_plan":analysis["action_plan"],
       
    
}
    