from database.database import SessionLocal
from fastapi import APIRouter,  HTTPException
from models.roles import Role
from core.logger import logger


router = APIRouter(
    tags=["Roles_id"]
)

@router.get("/roles_id/{roles_id}")
def get_roles(roles_id:int):
    logger.info(f"Fetching Role. Role ID: {roles_id}")    
    db = SessionLocal()
    
    try:
        roles = (
            db.query(Role)
            .filter(Role.role_id== roles_id)
            .first()
        )
        
        if roles is None:
            logger.warning(f"Roles not found. Analysis ID: {roles_id}")
            
            raise HTTPException(
                status_code=404,
                detail="Roles not found."
            )
        logger.info(f"Roles fetched successfully. Roles ID: {roles_id}")
    
    
        return {
        "role_id": roles.role_id,
        "role_name": roles.role_name,
        "description":roles.description,
        "knowledge_source": roles.knowledge_source
    }
    
    finally:
        db.close()
     
            