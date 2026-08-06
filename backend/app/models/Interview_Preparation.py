from database.database import Base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.sql import func


class Interview_Preparation(Base):
    __tablename__ = "interview_preparation"
    
    id = Column(
    Integer,
    primary_key=True,
    index=True
)

    role_id = Column(
        Integer,
        ForeignKey("roles.role_id"),
        nullable=False
    )

    skill = Column(
        String(100),
        nullable=False
    )

    question = Column(
        String(1000),
        nullable=False
    )

    question_type = Column(String(50), nullable=False)

    difficulty = Column(String(20), nullable=False)
    
    
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )
    
    