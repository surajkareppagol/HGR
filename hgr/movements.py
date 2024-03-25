import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision

model_path = "tasks/custom_gestures.task"
recognizer = vision.GestureRecognizer.create_from_model_path(model_path)

capture = cv2.VideoCapture(0)
top_gesture = None
rating = None
count = 0

while True:
    success, frame = capture.read()

    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

    recognition_result = recognizer.recognize(image)

    if len(recognition_result.gestures) > 0:
        top_gesture = recognition_result.gestures[0][0]

    if not top_gesture:
        result = "None"
        rating = 0.0
    else:
        result = top_gesture.category_name
        rating = top_gesture.score

    print(f"{count} Gesture recognized: {result} ({rating})")

    cv2.putText(
        frame,
        f"{result}",
        (0, 40),
        cv2.FONT_HERSHEY_PLAIN,
        3.0,
        (0, 0, 0),
        3,
    )

    cv2.imshow("img", frame)

    count += 1

    if cv2.waitKey(10) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
