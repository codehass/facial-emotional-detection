import sys
import os
import uuid, aiofiles

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from database import Base, engine
from app.routes import prediction_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Emotion Detection API", version="1.0.0")

app.include_router(prediction_routes.router)


@app.get("/", tags=["Root"])
async def root():
    return {"message": "Welcome to the Emotion Facial Detection API!"}
