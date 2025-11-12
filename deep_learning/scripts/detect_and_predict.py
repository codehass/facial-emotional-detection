import cv2
import cv2
import tensorflow as tf
import numpy as np

## load model, haarcascade, labels and image dimensions
facial_detection_model = tf.keras.models.load_model("emotion_face_detection.keras")
HARRAR_CASCADE_PATH = "haarcascade_frontalface_default.xml"
IMAGE_HEIGHT = 48
IMAGE_WIDTH = 48
emotion_labels = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]


def detect_and_predict(image_url):

    image = cv2.imread(image_url)

    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(HARRAR_CASCADE_PATH)

    if face_cascade.empty() == True:
        print("Le fichier n'est pas chargé: ", face_cascade.empty())
    else:
        print("Le fichier est chargé.")

    faces = face_cascade.detectMultiScale(
        image_gray, scaleFactor=1.3, minSize=(IMAGE_HEIGHT, IMAGE_WIDTH)
    )

    for x, y, width, height in faces:
        cv2.rectangle(
            image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2
        )

    # on sauvegarde l'image
    # cv2.imwrite("new.jpg", image)

    for x, y, w, h in faces:
        face = image[y : y + h, x : x + w]
        face_resized = cv2.resize(face, (48, 48))
        face_array = np.expand_dims(face_resized, axis=0)
        face_array = face_array.astype("float32") / 255.0

    predictions = facial_detection_model.predict(face_array)

    predicted_class = np.argmax(predictions[0])
    confidence = np.max(predictions[0])

    predicted_emotion = emotion_labels[predicted_class]

    for x, y, w, h in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(
            image,
            f"{predicted_emotion}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (36, 255, 12),
            2,
        )

    # cv2.imshow("Detected Face", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return [confidence, predicted_emotion]


print(detect_and_predict("girl.jpg"))
