from core.logger import logger
from fastapi import APIRouter
from services.progress_tracking_service import (
    get_progress,
    reset_progress,
    update_progress,
)

router = APIRouter(
        tags=["progress_tracking"]

)

@router.get("/progress_tracking/{resume_id}")
def get_progress_tracking(resume_id:int):
    logger.info(
        f"Progress request received. Resume ID: {resume_id}"
    )
    
    return get_progress(
        resume_id=resume_id
    )
    
    
@router.put("/progress_tracking/{resume_id}")    
def update_progress_tracking(
    resume_id:int, 
    progress: int,
    completed_skill: str | None = None,
    current_learning_stage: str | None = None
):
    logger.info(
        f"Progress update request received. "
        f"Resume ID: {resume_id}"
    )


    return update_progress(
        resume_id = resume_id,
        progress = progress,
        completed_skill=completed_skill,
        current_learning_stage = current_learning_stage 
    )

@router.post("/progress-tracking/{resume_id}/reset")
def reset_progress_tracking(resume_id: int):

    logger.info(
        f"Progress reset request received. "
        f"Resume ID: {resume_id}"
    )

    return reset_progress(
        resume_id=resume_id
    )
    
