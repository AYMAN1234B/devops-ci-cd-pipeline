
from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="DevOps CI/CD Production API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "DevOps CI/CD Pipeline Running 🚀"}