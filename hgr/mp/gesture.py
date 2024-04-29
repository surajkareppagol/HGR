import cv2 as cv
import mediapipe as mpipe
from mediapipe.tasks.python import vision
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from tracker import Tracker


class Gesture:
    def __init__(self, model_path=""):
        self.model_path = model_path
        self.recognizer = vision.GestureRecognizer.create_from_model_path(model_path)

    def get_gesture(self, image):
        image = mpipe.Image(image_format=mpipe.ImageFormat.SRGB, data=image)
        result = self.recognizer.recognize(image)

        if len(result.gestures) > 0:
            top_gesture = result.gestures[0][0]

            gesture = top_gesture.category_name
            score = top_gesture.score

            return gesture, score
        else:
            return None, None


def main():
    global iteration, console
    gesture = Gesture("tasks/models/hand_model.task")
    tracker = Tracker()

    console.clear()
    console.print(Panel("👍 Hand Gesture Recognition"))

    while True:
        success, frame = capture.read()

        if success:
            gesture_, score = gesture.get_gesture(frame)

            if gesture_ is not None:
                iteration += 1
                table.add_row(str(iteration), str(gesture_), str(score))
                console.print(
                    f"[bold green]Iteration[/bold green]: {iteration}\t[bold]{gesture_}[/bold]\t[bold]{round(score, 2)}[/bold]"  # type: ignore
                )

                cv.putText(
                    frame,
                    f"{gesture_.capitalize()}",  # type: ignore
                    (10, 70),
                    cv.FONT_HERSHEY_DUPLEX,
                    3,
                    (231, 76, 60),
                    3,
                )

            frame = tracker.detect_hands(frame)
            cv.imshow("img", frame)

            if cv.waitKey(10) & 0xFF == ord("q"):
                cv.destroyAllWindows()
                break

    capture.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    capture = cv.VideoCapture(0)

    console = Console()
    console.clear()

    table = Table(box=box.DOUBLE_EDGE, highlight=True)

    table.add_column("Iteration", justify="center")
    table.add_column("Gesture", justify="center")
    table.add_column("Score", justify="center")

    iteration = 0

    main()

    console.clear()
    console.print(table)
