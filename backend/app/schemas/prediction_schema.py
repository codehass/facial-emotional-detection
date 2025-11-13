from pydantic import BaseModel
from datetime import datetime


class PredictionResponse(BaseModel):
    id: int
    emotion: str
    confidence: float
    created_at: datetime

    class Config:
        orm_mode = True
