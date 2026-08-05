from database.database import Base , engine
from models.learning_resource import Learning_Resource
from models.roles import Role


Base.metadata.create_all(bind=engine)

print("Tables created successfully!")