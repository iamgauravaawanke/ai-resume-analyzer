import uuid

from database.database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Text,Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func


class CareerChat(Base):
    __tablename__ = "career_chat"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    resume_id = Column(
        Integer,
        ForeignKey("resume.id"),
        nullable=False
    )

    user_message = Column(Text, nullable=False)
    ai_response = Column(Text, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )