## Methods

# get_gestures()
# get_landmarks_image()
# draw_landmarks_image()
# get_landmark_image()
# get_gesture_image()

import train
from mp.gesture import Gesture
from mp.tracker import Tracker

tracker = Tracker()
gesture = Gesture("tasks/models/hand_model.task")


class API:
    def __init__(self):
        """Initializes the App class"""
        pass

    def get_gestures(self):
        return train.gestures

    def get_landmarks_image(self, image):
        image = tracker.detect_hands(image)
        landmarks = tracker.get_landmarks(image)
        return landmarks

    def draw_landmarks_image(self, image):
        return tracker.detect_hands(image)

    def get_landmark_image(self, image, landmark):
        image = tracker.detect_hands(image)
        landmarks = tracker.get_landmarks(image)

        if landmarks:
            return (landmarks[landmark][1], landmarks[landmark][2])
        return None

    def get_gesture_image(self, image):
        gesture_, score = gesture.get_gesture(image)
        return gesture_
