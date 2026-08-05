from models.analysis import Analysis
from database.database import SessionLocal
from core.logger import logger
from fastapi import APIRouter,  HTTPException
from models.roles import Role


def learning_roadmap_service(analysis_id:int , roles_id:int):
    logger.info(f"Fetching analysis. Analysis ID: {analysis_id}")
    logger.info(f"Fetching Role. Role ID: {roles_id}")    

    db = SessionLocal()
    try:
        
        analysis = (db.query(Analysis) .filter(Analysis.id == analysis_id) .first() )
       
        
        if analysis is None:
                    logger.warning(f"Analysis not found. Analysis ID: {analysis_id}")
        
                    raise HTTPException(
                        status_code=404,
                        detail="Analysis not found."
                    )
          
          
          
        roles = ( db.query(Role).filter(Role.role_id== roles_id) .first() )    
                
        if roles is None:
                    logger.warning(f"Roles not found. Analysis ID: {roles_id}")
                    
                    raise HTTPException(
                        status_code=404,
                        detail="Roles not found."
                    )            
                    
        logger.info(f"Analysis fetched successfully. Analysis ID: {analysis_id}")
        
        logger.info(f"Roles fetched successfully. Roles ID: {roles_id}")

        
        return{
            "analysis_id": analysis.id,
            "estimated_timeline":analysis.estimated_timeline.split(", "),
            "learning_roadmap":analysis.learning_roadmap,
            "role_id": roles.role_id,


        }
    finally:
        db.close()    



    