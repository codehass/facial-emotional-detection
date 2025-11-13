from sqlalchemy import Column, Integer, String, DateTime, func
from database import Base
from pydantic import BaseModel
from datetime import datetime, timezone


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    emotion = Column(String)
    confidence = Column(String)
    create_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )


# class PredictionResponse(BaseModel):
#     int: id
#     emotion: str
#     confidence: str
#     # create_at: DateTime
