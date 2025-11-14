import cv2
import numpy as np
import tensorflow as tf

# Load your pre-trained model (assuming it's a Keras model saved as .h5)
model = tf.keras.models.load_model("emotion_face_detection.keras")
emotion_labels = ["Angry", "Disgust", "Fear", "Happy", "Sad", "Surprise", "Neutral"]
# Define the input shape expected by the model (this should match the model's expected input size)
input_shape = (48, 48)  # Example: for image classification models, typically 224x224

# Start the webcam
cap = cv2.VideoCapture(0)

# Loop to read frames
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Resize the frame to match the input shape expected by the model
    frame_resized = cv2.resize(frame, input_shape)

    # Normalize the image (for most models, you need to scale the pixel values to [0, 1])
    frame_normalized = frame_resized / 255.0

    # Add batch dimension (Keras models expect a batch of images, so we add a dimension)
    frame_input = np.expand_dims(frame_normalized, axis=0)

    # Make prediction
    predictions = model.predict(frame_input)

    # Assuming it's a classification model, get the predicted class index
    predicted_class = np.argmax(predictions, axis=-1)

    # Display the predicted class on the frame
    cv2.putText(
        frame,
        f"Prediction: {emotion_labels[predicted_class[0]]}",
        (40, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )

    # Display the resulting frame
    cv2.imshow("Live Prediction", frame)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
