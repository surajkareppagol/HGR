import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision

model_path = "tasks/gesture_recognizer.task"
recognizer = vision.GestureRecognizer.create_from_model_path(model_path)

capture = cv2.VideoCapture(0)

while True:
    success, frame = capture.read()

    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

    recognition_result = recognizer.recognize(image)

    if len(recognition_result.gestures) > 0:
        top_gesture = recognition_result.gestures[0][0]

        gesture = top_gesture.category_name
        score = top_gesture.score

        print(f"Gesture recognized: {gesture} ({score})")

        cv2.putText(
            frame,
            f"{gesture}",
            (0, 40),
            cv2.FONT_HERSHEY_PLAIN,
            3.0,
            (0, 0, 0),
            3,
        )

    cv2.imshow("img", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
