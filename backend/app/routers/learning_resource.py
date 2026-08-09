from core.logger import logger
from fastapi import APIRouter
from services.learning_resource_service import learning_resources_service

router = APIRouter(
    tags=["Learning_Resources"]
)


@router.get("/learning_Resources/{analysis_id}")
def get_resources_roadmap(analysis_id: int):

    logger.info(
        f"Learning resources request received. Analysis ID: {analysis_id}"
    )

    return learning_resources_service(
        analysis_id=analysis_id
    )