from core.logger import logger
from fastapi import APIRouter
from schemas.career_chat import CareerChatRequest
from services.career_chat_service import (
    clear_conversation,
    get_chat_history,
    send_message,
)

router = APIRouter(
    tags=["career_chat"]
)


@router.post("/career_chat/{resume_id}")
def career_chat(
    resume_id: int,
    request: CareerChatRequest
):

    logger.info(
        f"Career Chat Request Received. "
        f"Resume ID: {resume_id}"
    )

    return send_message(
        resume_id=resume_id,
        user_message=request.message
    )
    
    
@router.get("/career_chat/{resume_id}") 
def get_all_chats(resume_id):
    logger.info(
        f"Career Chat History Request Received. "
        f"Resume ID: {resume_id}"
    )
    
    return get_chat_history(
        resume_id=resume_id
    )   
    
@router.delete("/career_chat/{resume_id}")
def delete_conversation(resume_id):
    logger.info(
            f"Career Delete History Request Received. "
            f"Resume ID: {resume_id}"
        )
    return clear_conversation(
        resume_id=resume_id
    )
         