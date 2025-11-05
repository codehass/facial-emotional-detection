from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import Base, engine, get_db, get_async_db
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()


Base.metadata.create_all(bind=engine)


# Create a new patient
@app.get("/")
async def get_home(db: AsyncSession = Depends(get_async_db)):
    return {"message": "Hello from ecome project"}
