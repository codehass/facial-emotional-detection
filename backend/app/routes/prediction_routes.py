from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from app.schemas.prediction_schema import PredictionResponse
from app.services.prediction_service import create_prediction_record
from app.models.prediction_model import Prediction

router = APIRouter(prefix="/predictions", tags=["Predictions"])


@router.post("/", response_model=PredictionResponse)
async def predict_emotion(file: UploadFile = File(...), db: Session = Depends(get_db)):
    valid_types = ["image/jpeg", "image/png", "image/jpg"]

    if file.content_type not in valid_types:
        raise HTTPException(status_code=400, detail="Only image files are allowed.")

    new_prediction = await create_prediction_record(file, db)
    new_prediction.confidence = float(new_prediction.confidence)

    return new_prediction


@router.get("/", response_model=list[PredictionResponse])
async def get_prediction_history(db: Session = Depends(get_db)):
    """Retrieve all previous predictions."""
    return db.query(Prediction).order_by(Prediction.created_at.desc()).all()
