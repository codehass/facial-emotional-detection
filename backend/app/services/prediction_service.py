import os
import uuid, aiofiles
from sqlalchemy.orm import Session
from app.models.prediction_model import Prediction
from deeplearning.scripts.detect_and_predict import emotion_detection


# save image temporary and return it's path
async def handle_image_upload(file):
    file_ext = file.filename.split(".")[-1]
    temp_filename = f"{uuid.uuid4()}.{file_ext}"

    async with aiofiles.open(temp_filename, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)

    return temp_filename


# process image and make a prediction
async def create_prediction_record(file, db: Session):
    temp_filename = await handle_image_upload(file)

    confidence, predicted_emotion = emotion_detection(temp_filename)

    if os.path.exists(temp_filename):
        os.remove(temp_filename)

    new_prediction = Prediction(emotion=predicted_emotion, confidence=str(confidence))

    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)

    return new_prediction
