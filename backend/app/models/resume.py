from datetime import datetime

from sqlalchemy import Column, Integer, String, LargeBinary, DateTime
from database.database import Base


class Resume(Base):
    __tablename__ = "resume"

    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String(255), nullable=False)
    file_data = Column(LargeBinary, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)