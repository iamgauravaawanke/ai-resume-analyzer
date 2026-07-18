from datetime import datetime

from sqlalchemy import Column, Integer, String, Text , LargeBinary, DateTime
from database.database import Base


class Role(Base):
    __tablename__ = "roles"
    
    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(100), nullable=False, unique=True)
    description = Column(Text, nullable=False)
    knowledge_source = Column(String(255), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    
    
    
    