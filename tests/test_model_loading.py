import os
import unittest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


class TestAPIPredictions(unittest.TestCase):

    def test_prediction_format(self):
        file_path = "tests/girl.jpg"
        # Check that the file exists
        self.assertTrue(os.path.isfile(file_path))

        with open(file_path, "rb") as img:
            response = client.post(
                "/predictions/", files={"file": ("girl.jpg", img, "image/jpg")}
            )

        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("id", data)
        self.assertIn("emotion", data)
        self.assertIn("confidence", data)
        self.assertIn("created_at", data)


if __name__ == "__main__":
    unittest.main()
