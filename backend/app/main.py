from fastapi import FastAPI
from database.database import Base, engine
import uvicorn
from models.resume import Resume
from models.analysis import Analysis
# from routers.upload_resume import resume_router

from routers.upload_resume import router as upload_router

from fastapi.middleware.cors import CORSMiddleware
from routers.analysis import router as analysis_router
from routers.roles import router as roles_router

app = FastAPI()


Base.metadata.create_all(bind=engine)



app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analysis_router)
app.include_router(upload_router)
app.include_router(roles_router)


if __name__=="__main__":
    uvicorn.run(app , port=8000)
    