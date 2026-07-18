from database.database import SessionLocal
from fastapi import HTTPException , APIRouter
from models.roles import Role
from core.logger import logger


router = APIRouter(
    tags=["Roles"]
)


@router.get("/roles")
def fetch_all_roles():
    
    logger.info(f"Fetching all Roles ")
    db = SessionLocal()
    
    try:
        roles = db.query(Role).all()
        
        if not roles:
        
            return{
                   "success": True,
                "message": "No roles found.",
                "data": []
            }
        
        
        return {
              "success": True,
            "message": "Roles fetched successfully.",
            "data": roles
        }
    except Exception as e:
        
        logger.error(f"Error fetching roles: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch roles."
        )
        
    
    finally:
        db.close()    

        
            
            
            

        
            