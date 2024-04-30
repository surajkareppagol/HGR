from json import loads

import cv2 as cv
from mp.api import API
from PIL import Image, ImageTk
from ui.util import set_image

api = API()


class Camera:
    def __init__(self):
        """Initializes the Camera class"""

        self.camera = cv.VideoCapture(0)
        self.detect = False
        self.gesture = "none"

    def get_frame(self):
        success, frame = self.camera.read()

        if success:
            return frame

    def convert_frame(self, frame, conversion=True):
        if conversion:
            return cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    def get_image(self, frame):
        image = Image.fromarray(frame)
        image = ImageTk.PhotoImage(image=image)

        return image

    def open_camera(self, window, label):
        frame = self.get_frame()
        if self.detect:
            image = api.draw_landmarks_image(frame)
            self.gesture = api.get_gesture_image(frame)

        frame = self.convert_frame(frame)
        image = self.get_image(frame)

        set_image(label, image)

        window.after(20, lambda: self.open_camera(window, label))

    def release(self):
        self.camera.release()

    def set_detect(self, detect):
        self.detect = True if detect else False

    def actions(self, detect):
        self.set_detect(detect)
        with open("hgr/ui/actions.json", "r") as file:
            actions = loads(file.read())

        print(self.gesture)

        if self.gesture in actions.keys():
            print(self.gesture)
