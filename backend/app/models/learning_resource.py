from enum import Enum as PyEnum
from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from database.database import Base


class ResourceType(PyEnum):
    VIDEO = "VIDEO"
    ARTICLE = "ARTICLE"
    DOCUMENTATION = "DOCUMENTATION"
    GITHUB = "GITHUB"
    COURSE = "COURSE"
    OTHER = "OTHER"



class Learning_Resource(Base):
    __tablename__ = "learning_resource"
    
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    skill = Column(String(255), nullable=False)

    resource_type = Column(Enum(ResourceType), nullable=False)

    title = Column(String(255), nullable=False)

    url = Column(String(500), nullable=False)

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
    
    