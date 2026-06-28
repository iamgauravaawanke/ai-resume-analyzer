from fastapi import APIRouter, UploadFile, File, HTTPException
import os
from pypdf import PdfReader
from core.logger import logger
from database.database import SessionLocal
from models.resume import Resume
router = APIRouter(
    tags=["Upload Resume"]
)

ALLOWED_EXTENSIONS = {".pdf"}

file_save_path = r"C:\Users\gaura\OneDrive\Documents\ai-resume-analyzer\backend\upload"

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

    save_path = os.path.join(file_save_path, file.filename)

    logger.info(f"Saving resume: {file.filename}")

    with open(save_path, "wb") as f:
        f.write(contents)

    logger.info("Resume saved successfully.")

    logger.info("Extracting text from PDF.")

    reader = PdfReader(save_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    logger.info(f"Text extraction completed. Characters extracted: {len(text)}")
    db = SessionLocal()

    resume = Resume(
        file_name=file.filename,
        file_data=contents
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    logger.info(f"Resume saved to database. Resume ID: {resume.id}")

    db.close()
    
    



    # print(text)

    return {
        "filename": file.filename,
        "content_type": file.content_type
    }