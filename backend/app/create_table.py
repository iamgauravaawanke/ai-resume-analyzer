from database.database import Base , engine
from models.Learning_Progress import LearningProgress
from models.analysis import Analysis
from models.resume import Resume


Base.metadata.create_all(bind=engine)

print("Tables created successfully!")