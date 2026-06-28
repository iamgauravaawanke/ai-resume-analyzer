from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+psycopg2://postgres:Gaurav%401234@localhost:5432/financial_health"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

# conn = get_db_connection()
# print("database connected suesfully")