import cv2
import mediapipe as mp
from landmarks import Tracker
from mediapipe.tasks.python import vision
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()
console.clear()

table = Table(box=box.DOUBLE_EDGE, highlight=True)

table.add_column("Iteration", justify="center")
table.add_column("Gesture", justify="center")
table.add_column("Score", justify="center")


tracker = Tracker()

model_path = "tasks/custom_model.task"
recognizer = vision.GestureRecognizer.create_from_model_path(model_path)

capture = cv2.VideoCapture(0)

console.clear()
console.print(Panel("👍 Hand Gesture Recognition"))

iteration = 0

while True:
    success, frame = capture.read()

    image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

    recognition_result = recognizer.recognize(image)

    if len(recognition_result.gestures) > 0:
        top_gesture = recognition_result.gestures[0][0]

        gesture = top_gesture.category_name
        score = top_gesture.score

        # print(f"Gesture recognized: {gesture} ({score})")
        iteration += 1

        table.add_row(str(iteration), str(gesture), str(score))
        console.print(
            f"[bold green]Iteration[/bold green]: {iteration}\t[bold]{gesture}[/bold]\t[bold]{round(score, 2)}[/bold]"
        )

        cv2.putText(
            frame,
            f"{gesture}",
            (0, 40),
            cv2.FONT_HERSHEY_PLAIN,
            3.0,
            (0, 0, 0),
            3,
        )

    frame = tracker.detect_hands(frame)
    cv2.imshow("img", frame)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

console.clear()
console.print(table)
