from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/home")
def demo():
    return{"msg": "susessfully creted fastapi"}


if __name__=="__main__":
    uvicorn.run(app , port=8000)
    