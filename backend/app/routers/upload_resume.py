from fastapi import APIRouter, UploadFile, File, HTTPException
import os

from core.logger import logger

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

    logger.info(f"Saving file: {file.filename}")

    with open(save_path, "wb") as f:
        f.write(contents)

    logger.info(f"Resume uploaded successfully: {file.filename}")

    return {
        "filename": file.filename,
        "content_type": file.content_type
    }