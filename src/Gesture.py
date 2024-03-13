import time

import cv2 as cv
import mediapipe as mp

from Tracker import Tracker

previous_time, current_time = 0, 0

capture = cv.VideoCapture(0)

tracker = Tracker(detection_confidence=0.7)

while True:
    success, img = capture.read()

    img = tracker.detect_hands(img)
    landmarks = tracker.get_landmarks(img)

    # Recognizing a gesture
    if landmarks:
        # LandmarkPosition_<coordinate>_<number>
        LP_X_4, LP_Y_4 = landmarks[4][1], landmarks[4][2]
        LP_X_8, LP_Y_8 = landmarks[8][1], landmarks[8][2]

        cv.circle(img, (LP_X_4, LP_Y_4), 15, (255, 0, 255), cv.FILLED)
        cv.circle(img, (LP_X_8, LP_Y_8), 15, (255, 0, 255), cv.FILLED)
        cv.line(img, (LP_X_4, LP_Y_4), (LP_X_8, LP_Y_8), (255, 0, 0), 3)

    current_time = time.time()
    FPS = int(1 // (current_time - previous_time))
    previous_time = current_time

    cv.putText(
        img, f"FPS: {FPS}", (10, 70), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 20), 2
    )

    cv.imshow("OpenRec", img)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
