import os
import unittest
import tensorflow as tf

MODEL_PATH = "./deeplearning/emotion_face_detection.keras"


class TestModel(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Load the model once for all tests."""
        if os.path.isfile(MODEL_PATH):
            cls.model = tf.keras.models.load_model(MODEL_PATH)
        else:
            cls.model = None

    def test_model_file_exists(self):
        """Ensure the model file exists."""
        self.assertTrue(os.path.isfile(MODEL_PATH))

    def test_model_load_successfully(self):
        """Ensure the model loads successfully."""
        self.assertIsNotNone(self.model)
        self.assertIsInstance(self.model, tf.keras.Model)


if __name__ == "__main__":
    unittest.main()
