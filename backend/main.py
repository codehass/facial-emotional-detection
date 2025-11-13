import sys
import os
import uuid, shutil, aiofiles

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from app.models.prediction_model import Prediction
from deeplearning.scripts.detect_and_predict import emotion_detection
from sqlalchemy import func


app = FastAPI()

Base.metadata.create_all(bind=engine)


# Create main route endpoint
@app.get("/")
async def get_home():
    return {"message": "Hello emotion facial detection API"}


# create prediction endpoint
@app.post("/predictions")
async def create_prediction(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    images_type = ["image/jpeg", "image/png", "image/jpg"]

    if file.content_type not in images_type:
        raise HTTPException(status_code=400, detail="Only image files are allowed.")

    file_ext = file.filename.split(".")[-1]
    temp_filename = f"{uuid.uuid4()}.{file_ext}"

    async with aiofiles.open(temp_filename, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)

    confidence, predicted_emotion = emotion_detection(temp_filename)

    if os.path.exists(temp_filename):
        os.remove(temp_filename)

    new_prediction = Prediction(emotion=predicted_emotion, confidence=str(confidence))
    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)

    confidence = float(confidence)

    return {
        "emotion": predicted_emotion,
        "confidence": confidence,
    }
