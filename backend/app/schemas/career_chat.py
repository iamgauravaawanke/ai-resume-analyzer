from pydantic import BaseModel


class CareerChatRequest(BaseModel):
    message: str