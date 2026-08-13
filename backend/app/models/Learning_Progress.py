from database.database import Base
from models.analysis import Analysis
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, String, Text, func


class LearningProgress(Base):
    
    __tablename__ = "learning_progress"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    
    resume_id = Column(
    Integer,
    ForeignKey("resume.id"),
    nullable=False
)
    progress = Column(
        Integer,
        nullable=False,
        default=0
    )  # Percentage (0-100)
    
    completed_skill = Column(
        Text,
        nullable=True
    )

    current_learning_stage = Column(
        String(100),
        nullable=False
    )  # Beginner, Intermediate, Advanced

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
    
