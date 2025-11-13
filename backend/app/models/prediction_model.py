from sqlalchemy import Column, Integer, String, DateTime, Float
from database import Base
from pydantic import BaseModel
from datetime import datetime, timezone


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    emotion = Column(String, nullable=False)
    confidence = Column(Float, nullable=False)
    created_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
