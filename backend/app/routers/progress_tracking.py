from core.logger import logger
from fastapi import APIRouter
from services.progress_tracking_service import (
    get_progress,
    reset_progress,
    update_progress,
)


router = APIRouter(
        tags=["Progress Tracking"]

)

@router.get("/progress_tracking/{resume_id}")
def get_progress_tracking(resume_id:int):
    logger.info(
        f"Progress request received. Resume ID: {resume_id}"
    )
    
    return get_progress(
        resume_id=resume_id
    )
    
@    