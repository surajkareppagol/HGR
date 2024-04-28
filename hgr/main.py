import tkinter as tk

import ttkbootstrap as ttk
import ui.layout
from camera import Camera
from ui.layout import layout_main
from ui.util import get_dimensions, get_icon, set_font


class App(ttk.Window):
    def __init__(self):
        """Initializes the App class"""

        super().__init__(themename="darkly")

        self.title("👍 HGR - Hand Gesture Recognizer")
        self.iconphoto(False, get_icon("assets/icon.png"))

        # Set Screen Size
        self.width, self.height = get_dimensions(self)
        self.geometry(f"{self.width}x{self.height}")

        self.bind("<Escape>", lambda _: self.quit())

        # Set Default Font
        set_font()

        # Create Main Layout
        layout_main(self, (self.width, self.height))

        # Call open_camera
        camera.open_camera(self, ui.layout.camera_L)

        self.mainloop()

        camera.open_camera(self, None, release=True)


if __name__ == "__main__":
    camera = Camera()
    App()
