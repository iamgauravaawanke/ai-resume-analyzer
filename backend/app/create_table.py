from database.database import Base , engine
from models.Interview_Preparation import Interview_Preparation
from models.roles import Role


Base.metadata.create_all(bind=engine)

print("Tables created successfully!")