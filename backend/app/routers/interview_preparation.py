from core.logger import logger
from fastapi import APIRouter
from services.interview_prepration import get_interview_preparation_service

router = APIRouter(
    tags = ["interview_preparation"]
)
@router.get("/interview-preparation/{role_id}")
def get_interview_preparation(role_id:int , skill:str | None = None ,  difficulty:str  | None = None , question_type:str |None = None):
    
    
    logger.info(
        f"Interview preparation request received. "
        f"Role ID: {role_id}, "
        f"Skill: {skill}, "
        f"Difficulty: {difficulty}, "
        f"Question Type: {question_type}"
    )
    
    return get_interview_preparation_service(
        role_id=role_id,
        difficulty=difficulty,
        skill=skill,
        question_type=question_type
        
    )
 

