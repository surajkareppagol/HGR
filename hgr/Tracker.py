import time

import cv2 as cv
import mediapipe as mp


class Tracker:
    def __init__(
        self,
        mode=False,
        hands=2,
        complexity=1,
        detection_confidence=0.5,
        track_confidence=0.5,
    ) -> None:
        self.mode = mode
        self.hands = hands
        self.complexity = complexity
        self.detection_confidence = detection_confidence
        self.track_confidence = track_confidence

        self.mp_hands = mp.solutions.hands

        self.hands = self.mp_hands.Hands(
            self.mode,
            self.hands,
            self.complexity,
            self.detection_confidence,
            self.track_confidence,
        )

        # print(help(self.mp_hands.Hands()))

        self.mp_draw = mp.solutions.drawing_utils

    def detect_hands(self, img, draw=True):
        img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        self.hand_landmarks = self.hands.process(img_rgb).multi_hand_landmarks

        if self.hand_landmarks:
            for hand_landmark in self.hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        img, hand_landmark, self.mp_hands.HAND_CONNECTIONS
                    )
        return img

    def get_landmarks(self, img, hand=0, draw=False):
        landmarks = []

        if self.hand_landmarks:
            current_hand = self.hand_landmarks[hand]

            for id, landmark in enumerate(current_hand.landmark):
                # print(f"ID: {id}\nLand Marks:\n{landmark}")
                height, width, channels = img.shape
                pos_x, pos_y = int(landmark.x * width), int(landmark.y * height)

                landmarks.append([id, pos_x, pos_y])

                if draw:
                    print(f"ID: {id}\nPosition X: {pos_x}\nPosition Y: {pos_y}")

        return landmarks


def main():
    previous_time, current_time = 0, 0

    capture = cv.VideoCapture(0)

    tracker = Tracker()

    while True:
        success, img = capture.read()

        img = tracker.detect_hands(img)
        landmarks = tracker.get_landmarks(img)

        if landmarks:
            LP_X_8, LP_Y_8 = landmarks[8][1], landmarks[8][2]
            cv.circle(img, (LP_X_8, LP_Y_8), 15, (255, 0, 255), cv.FILLED)

            print(LP_X_8, LP_Y_8)

        current_time = time.time()
        FPS = int(1 // (current_time - previous_time))
        previous_time = current_time

        cv.putText(
            img, f"FPS: {FPS}", (10, 70), cv.FONT_HERSHEY_TRIPLEX, 3, (255, 255, 255), 3
        )

        cv.imshow("OpenRec", img)

        if cv.waitKey(1) & 0xFF == ord("q"):
            break


if __name__ == "__main__":
    main()
