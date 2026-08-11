from core.logger import logger
from database.database import SessionLocal
from fastapi import APIRouter, HTTPException
from models.analysis import Analysis
from models.Interview_Preparation import Interview_Preparation
from models.roles import Role


def get_interview_preparation_service(role_id:int , skill:str ,  difficulty:str , question_type:str):
    logger.info(f"Fetching Interview Preparation for Role ID:{role_id} , skill:{skill} , difficulty:{difficulty} , question_type:{question_type}")
    
    db = SessionLocal()
    try:
        
        roles = (db.query(Role).filter(Role.role_id==role_id) .first())
        if roles is None:
            
                logger.warning(f"Roles not found. Analysis ID: {role_id}")
                raise HTTPException(
                    status_code=404,
                    detail = "Roles not found"
                )
        logger.info(f"Roles fetched successfully. Roles ID: {roles.role_id}")
       
        query  = (db.query(Interview_Preparation).filter(
            
            Interview_Preparation.role_id == role_id,
        ))
        if skill:
            query  = query.filter(Interview_Preparation.skill == skill)
        
        if difficulty:
            query = query.filter(Interview_Preparation.difficulty == difficulty)
            
        if question_type:
            query = query.filter(Interview_Preparation.question_type == question_type)    
                
        questions= query.all()    
        
        # Build REsponse
        response = {
            "role_id":role_id,
            "questions" :[]
        }
        
        for question in questions:
            response["questions"].append({
                "id":question["id"],
                "skill":question["skill"],
                "question":question["question"],
                "question_type":question["question_type"],
                "difficulty":question["difficulty"]
                
            })
        return response
    except Exception as e:
        
        logger.exception(
            f"Error fetching Interview Preparation "
            f"for Role ID: {role_id}: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to fetch interview preparation"
        )

    finally:

        db.close()