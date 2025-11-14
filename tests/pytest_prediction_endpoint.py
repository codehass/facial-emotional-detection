import os
from fastapi.testclient import TestClient
from backend.main import app

MODEL_PATH = "./deeplearning/emotion_face_detection.keras"


client = TestClient(app)


def test_prediction_format():

    file_path = "tests/girl.jpg"
    assert os.path.isfile(file_path)

    with open(file_path, "rb") as img:
        response = client.post(
            "/predictions/", files={"file": ("girl.jpg", img, "image/jpg")}
        )

    assert response.status_code == 200
    # data = response.json()

    # assert "id" in data
