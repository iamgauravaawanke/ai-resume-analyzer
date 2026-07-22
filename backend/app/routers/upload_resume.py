from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import json
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from core.logger import logger
from database.database import SessionLocal
from models.resume import Resume
from models.analysis import Analysis
from services.ai_service import ask_llm
from utils.json_utils import clean_json_response
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from models.roles import Role
#  PASTE THIS LINE INSTEAD
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from pathlib import Path



router = APIRouter(
    tags=["Upload Resume"],
    
)

ALLOWED_EXTENSIONS = {".pdf"}

FILE_SAVE_PATH = r"C:\Users\gaura\OneDrive\Documents\ai-resume-analyzer\backend\upload"


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

    logger.info(f"Resume uploaded successfully: {file.filename}")

    reader = PdfReader(save_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    logger.info(f"Resume text extracted ({len(text)} characters).")

    db = SessionLocal()

    try:
        # ---------------------------
        # Save Resume
        # ---------------------------
        resume = Resume(
            file_name=file.filename,
            file_data=contents
        )

        db.add(resume)
        db.commit()
        db.refresh(resume)

        logger.info(f"Resume stored in database. Resume ID: {resume.id}")

        # ---------------------------
        # AI Analysis
        # ---------------------------
        logger.info("Sending resume to Qwen for analysis.")
        
        selected_role = "Backend Developer"   # Temporary
    
        role_id = 1
        
 
        role = db.query(Role).filter(Role.role_id == role_id).first()
        
        
        print("role==================" , role)
        if not role:
            raise HTTPException(status_code=404 , detail="Role Not Found")
        
        selected_role = role.role_name
        
        
        print("selected role==== ", selected_role)
        
        BASE_DIR = Path(__file__).resolve().parent.parent
        # print(BASE_DIR)
        KNOWLEDGE_DIR = BASE_DIR / "knowledge"
        # print(KNOWLEDGE_DIR)
        
        knoweldge_file_path = KNOWLEDGE_DIR / role.knowledge_file
        
        print("knoweldge_file_path====================", knoweldge_file_path)
        
        if not knoweldge_file_path.exists():
            raise HTTPException(
                status_code=404, 
                detail=f"Knowledge file '{role.knowledge_file}' not found."
            )
            
        reader1 = PdfReader(knoweldge_file_path)
        
        text1 = ""
        
        
        for i, page in enumerate(reader1.pages):
            print("Reading page", i + 1)

        page_text = page.extract_text()

        print("Extracted:", page_text is not None)

        if page_text:
            text1 += page_text

        print("Final Length:", len(text1))

        text_splitter  = RecursiveCharacterTextSplitter(
            chunk_size = 100,
            chunk_overlap = 0
        )
        
        split_texts = text_splitter .split_text(text1)
        print("split_text=================" , split_texts)
        
            
        role_knowledge=""
        analysis = ask_llm(
            resume_text=text,
            selected_role=selected_role,
            role_knowledge=role_knowledge)
        
        analysis = clean_json_response(analysis)
        

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

        db.add(analysis_db)
        db.commit()
        db.refresh(analysis_db)
        resume_id = resume.id
        analysis_id = analysis_db.id

        logger.info(
            f"Analysis stored in database. Analysis ID: {analysis_db.id}"
        )

    finally:
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
    