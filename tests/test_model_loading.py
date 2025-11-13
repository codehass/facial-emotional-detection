import pytest
import os
import tensorflow as tf

MODEL_PATH = "emotion_face_detection.keras"


@pytest.fixture
def model():
    """Fixture to load the model."""
    model = tf.keras.models.load_model(MODEL_PATH)
    return model


def test_model_file_exists():
    """Test to ensure the model file exists."""
    assert os.path.isfile(MODEL_PATH)


def test_model_load_successfully(model):
    """Test to ensure the model loads successfully."""
    assert isinstance(model, tf.keras.Model)
