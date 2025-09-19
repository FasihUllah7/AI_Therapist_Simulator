from fastapi import FastAPI
from .routes import router

app = FastAPI(title="AI Therapist Simulator")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "AI Therapist API is running 🚀"}
