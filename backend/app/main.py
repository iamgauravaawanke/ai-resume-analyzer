import uvicorn
from database.database import Base, engine
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.analysis import router as analysis_router
from routers.career_chat import router as career_chat_router
from routers.interview_preparation import router as interview_preparation
from routers.learning_resource import router as learning_Resources_router
from routers.learning_roadmap import router as learning_roadmap_router
from routers.progress_tracking import router as progress_tracking_router
from routers.roles import router as roles_router
from routers.roles_id import router as role_id_router

# from routers.upload_resume import resume_router
from routers.upload_resume import router as upload_router

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
app.include_router(role_id_router)
app.include_router(learning_roadmap_router)
app.include_router(learning_Resources_router)
app.include_router(interview_preparation)
app.include_router(progress_tracking_router)
app.include_router(career_chat_router)



if __name__=="__main__":
    uvicorn.run(app , port=8000)
    