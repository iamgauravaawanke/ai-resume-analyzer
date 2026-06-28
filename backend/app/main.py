from fastapi import FastAPI
from database.database import Base, engine
import uvicorn
from models.resume import Resume
from models.analysis import Analysis
from routers.upload_resume import router


app = FastAPI()


Base.metadata.create_all(bind=engine)
app.include_router(router)



if __name__=="__main__":
    uvicorn.run(app , port=8000)
    