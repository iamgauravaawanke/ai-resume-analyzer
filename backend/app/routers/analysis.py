from database.database import SessionLocal
from fastapi import APIRouter, UploadFile, File, HTTPException
from models.analysis import Analysis
from core.logger import logger

router = APIRouter(
    tags= ["Analysis"]
)

    
# 5. API Endpoint: Fetch One User by ID
@router.get("/analysis/{analysis_id}")
def get_analysis(analysis_id: int):

    logger.info(f"Fetching analysis. Analysis ID: {analysis_id}")

    db = SessionLocal()

    try:
        analysis = (
            db.query(Analysis)
            .filter(Analysis.id == analysis_id)
            .first()
        )

        if analysis is None:
            logger.warning(f"Analysis not found. Analysis ID: {analysis_id}")

            raise HTTPException(
                status_code=404,
                detail="Analysis not found."
            )

        logger.info(f"Analysis fetched successfully. Analysis ID: {analysis_id}")

        return {
            "analysis_id": analysis.id,
            "resume_id": analysis.resume_id,
            "ats_score": analysis.ats_score,
            "summary": analysis.summary,
            "technical_skills": analysis.technical_skills.split(", "),
            "soft_skills": analysis.soft_skills.split(", "),
            "missing_skills": analysis.missing_skills.split(", "),
            "suggestions": analysis.suggestions.split("\n")
        }

    finally:
        db.close()