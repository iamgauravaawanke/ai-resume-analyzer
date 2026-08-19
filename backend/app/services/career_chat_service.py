from core.logger import logger
from database.database import SessionLocal
from fastapi import APIRouter, HTTPException
from models.analysis import Analysis


def get_analysis(resume_id:int):
    logger.info(f"Fetching  analysis i=using this resume_id {resume_id}")
    
    db = SessionLocal()
    try:
        analysis = (
            db.query(Analysis).filter(Analysis.resume_id==resume_id).first()
        )
        if analysis is None:
            logger.warning(
                f"Analysis not found for Resume ID: {resume_id}")
            
            raise HTTPException (
                status_code=404,
                detail="Analysis Not Found"
            )
        
        logger.info(f"analaysis  found for this resume_id and resume{resume_id}") 
        
        return analysis
    except HTTPException:
        raise
    except Exception as e:
        
        logger.exception(
            f"Error fetching analysis for "
            f"resume_id {resume_id}: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to fetch analysis"
        )

        
    finally:
        db.close()    
        
def build_career_context(analysis):
    
    logger.info(
        f"Building career context for analysis ID: {analysis.id}"
    )

    career_context = {
        "role_id": analysis.role_id,
        "summary": analysis.summary,
        "technical_skills": analysis.technical_skills,
        "soft_skills": analysis.soft_skills,
        "missing_skills": analysis.missing_skills,
        "suggestions": analysis.suggestions,
        "learning_roadmap": analysis.learning_roadmap,
        "suggested_projects": analysis.suggested_projects,
        "estimated_timeline": analysis.estimated_timeline,
        "action_plan": analysis.action_plan,
    }

    logger.info(
        f"Career context built successfully "
        f"for analysis ID: {analysis.id}"
    )

    return career_context  