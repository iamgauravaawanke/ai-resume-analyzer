from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import json

from pypdf import PdfReader

from core.logger import logger
from database.database import SessionLocal
from models.resume import Resume
from models.analysis import Analysis
from services.ai_service import ask_llm
from utils.json_utils import clean_json_response
from sqlalchemy.orm import declarative_base, sessionmaker, Session




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

        analysis = ask_llm(text)
        analysis = clean_json_response(analysis)
        

        logger.info("AI analysis completed.")
        # print(repr(analysis))
        
        logger.info(f"Qwen Response:\n{analysis}")

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
            missing_skills=", ".join(analysis["missing_skills"]),
            # suggestions=", ".join(analysis["suggestions"]),
            suggestions="\n".join(
    f"{item['skill']} - {item['reasoning']}"
    for item in analysis["suggestions"]
)
            
            
            ## gamma 
            
#         suggestions="\n".join(
#     f"{item['title']} - {item['description']}"
#     for item in analysis["suggestions"]
# )    
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
    "soft_skills":analysis["soft_skills"]
    
    
    
    
}
    