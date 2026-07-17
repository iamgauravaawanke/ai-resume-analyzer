from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+psycopg2://postgres:Gaurav%401234@localhost:5432/financial_health"
engine = create_engine(DATABASE_URL)

Base = declarative_base()


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)




# print("database connected suesfully")