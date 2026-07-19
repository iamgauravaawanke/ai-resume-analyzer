from database.database import Base , engine
from models.analysis import Analysis

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")