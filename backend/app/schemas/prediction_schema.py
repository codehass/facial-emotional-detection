from pydantic import BaseModel, ConfigDict
from datetime import datetime


class PredictionResponse(BaseModel):
    id: int
    emotion: str
    confidence: float
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
