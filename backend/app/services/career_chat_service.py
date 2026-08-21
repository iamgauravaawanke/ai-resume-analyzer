from core.llm import ask_qwen
from core.logger import logger
from database.database import SessionLocal
from fastapi import APIRouter, HTTPException
from models.analysis import Analysis
from models.CareerChat import CareerChat
from models.roles import Role


def get_analysis(resume_id: int):

    logger.info(
        f"Fetching analysis using Resume ID: {resume_id}"
    )

    db = SessionLocal()

    try:

        analysis = (
            db.query(Analysis)
            .filter(Analysis.resume_id == resume_id)
            .first()
        )

        if analysis is None:

            logger.warning(
                f"Analysis not found for Resume ID: {resume_id}"
            )

            raise HTTPException(
                status_code=404,
                detail="Analysis not found"
            )

        # Get role_id from the Analysis record
        role_id = analysis.role_id

        role = (
            db.query(Role)
            .filter(Role.role_id == role_id)
            .first()
        )

        if role is None:

            logger.warning(
                f"Role not found for Role ID: {role_id}"
            )

            raise HTTPException(
                status_code=404,
                detail="Role not found"
            )

        logger.info(
            f"Analysis and Role found successfully. "
            f"Resume ID: {resume_id}, "
            f"Role: {role.role_name}"
        )

        return analysis, role

    except HTTPException:
        raise

    except Exception as e:

        db.rollback()

        logger.exception(
            f"Error fetching analysis for "
            f"Resume ID {resume_id}: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to fetch analysis"
        )

    finally:
        db.close()   
        
def build_career_context(analysis ,role):
    
    logger.info(
        f"Building career context for analysis ID: {analysis.id}"
    )

    career_context = {
        "role_id": analysis.role_id,
        "role": role.role_name,
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

def call_ai(career_context, user_message):

    logger.info("AI career chat request started.")

    role = career_context["role"]

    prompt = f"""
You are an AI Career Coach for a {role}.

Use the following career context to answer the user's question.

Career Context:
{career_context}

User Message:
{user_message}

Give a clear, practical, and personalized answer based on the career context.
"""

    logger.info(
        f"Sending career context to AI for role: {role}"
    )

    try:

        ai_response = ask_qwen(prompt)

        logger.info(
            "AI career chat response received successfully."
        )

        return ai_response

    except Exception as e:

        logger.exception(
            f"Error while calling AI service: {e}"
        )

        raise
def save_chat_history(resume_id:int , user_message:str , ai_response:str):
    logger.info(f"save chat history function started ")
    
    db = SessionLocal()
    try:
        chat = CareerChat(
            resume_id = resume_id,
            user_message = user_message,
            ai_response = ai_response
        )
        db.add(chat)
        db.commit()
        db.refresh(chat)
        
        logger.info("Carrer Chat saved sussfully"
                    f" for this resume_id : {resume_id}")
        
        return chat
    
    except Exception as e:
        db.rollback()
        logger.exception(f"Error occur during saving carrer chat in db "
                         f"for Resume_id : {resume_id}: {e}" 
                         )
        
        raise HTTPException(
            status_code = 500, 
            detail = "Failed to saved carrer chat"
        )
    finally:
        db.close()
            
def send_message(resume_id, user_message):
    
    logger.info(
        f"Send message started for Resume ID: {resume_id}"
    )

    analysis, role = get_analysis(resume_id)

    career_context = build_career_context(
        analysis,
        role
    )

    ai_response = call_ai(
        career_context,
        user_message
    )

    saved_chat = save_chat_history(
        resume_id,
        user_message,
        ai_response
    )

    logger.info(
        f"Career chat completed for Resume ID: {resume_id}"
    )

    return saved_chat
                     

def  get_chat_history(resume_id):
    logger.info("Inside Get Chat History Function")
    
    db = SessionLocal()
    try:
        chats = db.query(CareerChat).filter(CareerChat.resume_id==resume_id).order_by(CareerChat.created_at.asc()).all() 
        
        logger.info(
            f"Found {len(chats)} chat records "
            f"for Resume ID: {resume_id}")
        
        history = []
        
        for chat in chats:

            history.append({
                "user_message": chat.user_message,
                "ai_response": chat.ai_response
            })

        return {
            "resume_id": resume_id,
            "history": history
        }

    except Exception as e:

        db.rollback()

        logger.exception(
            f"Error fetching career chat history "
            f"for Resume ID {resume_id}: {e}"
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to fetch career chat history"
        )

    finally:

        db.close()