from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from database.database import Base


class Analysis(Base):
    __tablename__ = "analysis"

    id = Column(Integer, primary_key=True, autoincrement=True)
    resume_id = Column(Integer, ForeignKey("resume.id"), nullable=False)
    
        # NEW: Foreign key to roles table
    role_id = Column(Integer, ForeignKey("roles.role_id"), nullable=False)
    
    ats_score = Column(Integer, nullable=False)
    summary = Column(String, nullable=False)
    technical_skills = Column(String, nullable=False)
    soft_skills = Column(String, nullable=False)
    missing_skills = Column(String, nullable=False)
    suggestions = Column(String, nullable=False)
    
    learning_roadmap  = Column(Text ,nullable=True )
    suggested_projects = Column(Text , nullable=True)
    estimated_timeline = Column(Text, nullable=True)
    action_plan = Column(Text, nullable=True)

    
    created_at = Column(DateTime, default=datetime.utcnow)