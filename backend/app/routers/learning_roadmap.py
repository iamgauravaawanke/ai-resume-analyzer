from fastapi import APIRouter,  HTTPException
from core.logger import logger
from services.learning_roadmap_service import learning_roadmap_service


router = APIRouter(
    tags=["Learning_Roadmap"]
)

@router.get("/learning_roadmap/{analysis_id}")
def get_learning_roadmap(analysis_id:int , roles_id:int):
    logger.info(
        f"Learning roadmap request received. Analysis ID: {analysis_id}, Role ID: {roles_id}"
    )
    
    return learning_roadmap_service(
        analysis_id=analysis_id,
        roles_id= roles_id
    )