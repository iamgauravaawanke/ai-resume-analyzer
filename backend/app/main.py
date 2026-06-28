from fastapi import FastAPI
from database.database import Base, engine
import uvicorn
from models.resume import Resume
from models.analysis import Analysis


app = FastAPI()

@app.post("/home")
def demo():
    return{"msg": "susessfully creted fastapi"}


Base.metadata.create_all(bind=engine)
print("database created susefully")


if __name__=="__main__":
    uvicorn.run(app , port=8000)
    