import tkinter as tk
from pprint import pprint
from tkinter import filedialog

import cv2 as cv
import ttkbootstrap as ttk
from landmarks import Tracker
from PIL import Image, ImageTk
from rich.console import Console
from rich.panel import Panel


class UI(Tracker):
    def __init__(self):
        super().__init__()

        self.hgr_actions = {}
        self.hgr_actions_count = 0
        self.cam = cv.VideoCapture(0)

        self.tracker = False

        self.training_data_directory = ""

    def landmarks(self, img):
        img = super().detect_hands(img)
        img = super().get_landmarks(img)

        return img

    def get_directory_name(self, path="", browse=True):
        if browse:
            self.training_data_directory = filedialog.askdirectory()
        else:
            self.training_data_directory = path

    def create_train_window(self):
        self.train_window = tk.Toplevel()

        self.train_window.iconphoto(False, self.img)

        self.train_window.title("Train Model")
        self.train_window.geometry(f"{self.window_size[0]}x{self.window_size[1]}")

        # Label
        train_window_label = tk.Label(
            master=self.train_window, text="Train Model", font=("Fira Code", 20)
        )
        train_window_label.pack()

        # Frame
        train_window_file_frame = tk.Frame(master=self.train_window)

        # Label
        train_window_directory_entry_var = tk.StringVar()
        train_window_directory_entry = tk.Entry(
            master=train_window_file_frame,
            textvariable=train_window_directory_entry_var,
            font=("Fira Code", 20),
            width=40,
        )

        train_window_directory_entry.pack(side="left", padx=40)

        # Button
        train_window_ok_button = tk.Button(
            master=train_window_file_frame,
            text="Ok",
            font=("Fira Code", 20),
            command=lambda: self.get_directory_name(
                train_window_directory_entry_var.get(), browse=False
            ),
        )

        train_window_directory_button = tk.Button(
            master=train_window_file_frame,
            text="Browse",
            font=("Fira Code", 20),
            command=lambda: self.get_directory_name(),
        )

        train_window_ok_button.pack(side="left", padx=10)
        train_window_directory_button.pack(side="left", padx=10)

        train_window_file_frame.pack(anchor="center", pady=40)

        # Label
        train_window_directory_label = tk.Label(
            master=self.train_window,
            text="self.training_data_directory",
            font=("Fira Code", 20),
        )
        train_window_directory_label.pack(pady=20)

        self.train_window.mainloop()

    def get_width_height(self, window):
        return (window.winfo_screenwidth(), window.winfo_screenheight())

    def toggle_detection(self):
        self.tracker = True if not self.tracker else False

    def create_main_window(self, icon, title="TK App"):
        self.window = ttk.Window(themename="darkly")
        self.icon = icon

        self.img = tk.PhotoImage(file=self.icon)
        self.window.iconphoto(False, self.img)
        self.window.title(title)

        self.window_size = self.get_width_height(self.window)
        self.window.geometry(f"{self.window_size[0]}x{self.window_size[1]}")

        # Label
        window_cam_label = tk.Label(
            master=self.window, text="", anchor="center", pady=20
        )
        window_cam_label.pack(fill="both", expand=True)

        # Frame
        windows_button_frame = tk.Frame(master=self.window, padx=20, pady=80)

        # Button
        window_start_button = tk.Button(
            master=windows_button_frame,
            text="Start HGR",
            font=("Fira Code", 20),
            command=lambda: self.toggle_detection(),
        )

        window_end_button = tk.Button(
            master=windows_button_frame, text="End HGR", font=("Fira Code", 20)
        )

        window_action_button = tk.Button(
            master=windows_button_frame,
            text="Set Actions",
            font=("Fira Code", 20),
            command=lambda: self.create_sub_window(),
        )

        window_train_button = tk.Button(
            master=windows_button_frame,
            text="Train Model",
            font=("Fira Code", 20),
            command=lambda: self.create_train_window(),
        )

        window_start_button.pack(side="left")
        window_end_button.pack(side="left", padx=10)
        window_action_button.pack(side="left", padx=20)
        window_train_button.pack(side="left", padx=10)

        windows_button_frame.pack()

        window_end_button.bind("<Button-1>", lambda e: self.window.quit())

        self.open_cam(window_cam_label)

        self.window.bind("<Escape>", lambda e: self.window.quit())

        self.window.mainloop()

        self.cam.release()

    def open_cam(self, container):
        success, frame = self.cam.read()

        if success:
            if self.tracker:
                self.frame = super().detect_hands(frame)
                # self.frame = super().get_landmarks(frame)

            self.frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

            image = Image.fromarray(self.frame)
            image = ImageTk.PhotoImage(image=image)

            container.photo = image  # type: ignore

            container.configure(image=image)

        self.window.after(20, lambda: self.open_cam(container))

    def add_action(self, points, action, entry=None, button=None):
        self.hgr_actions[points] = action

        if entry and button:
            entry.config(state="disabled")
            button.config(state="disabled")

    def add_action_widgets(self, window, x=0, y=0):
        if self.hgr_actions_count == 8:
            return

        # Frame
        widget_action_frame = tk.Frame(master=window)

        # Label
        widget_action_label = tk.Label(
            master=widget_action_frame, text=f"({x}, {y})", font=("Fira Code", 20)
        )
        widget_action_label.pack(side="left", padx=40, expand=True, fill="x")

        self.add_action(f"({x}, {y})", "ls")

        # Entry
        widget_action_entry_var = tk.StringVar()
        widget_action_entry = tk.Entry(
            master=widget_action_frame,
            textvariable=widget_action_entry_var,
            font=("Fira Code", 20),
        )
        widget_action_entry.pack(side="left", padx=20)

        # Button
        widget_action_button = tk.Button(
            master=widget_action_frame,
            text="Add",
            font=("Fira Code", 20),
            command=lambda: self.add_action(
                f"({x}, {y})",
                widget_action_entry_var.get(),
                widget_action_entry,
                widget_action_button,
            ),
        )

        widget_action_button.pack(side="left", padx=20)

        widget_action_frame.pack(pady=10, anchor="center")

        self.hgr_actions_count += 1

    def sub_window_buttons_action(self, close, window):
        if close:
            self.hgr_actions = {}
        self.hgr_actions_count = 0

        window.destroy()
        pprint(self.hgr_actions)

    def create_sub_window(self):
        self.sub_window = tk.Toplevel()

        self.sub_window.iconphoto(False, self.img)

        self.sub_window.title("Actions")
        self.sub_window.geometry(f"{self.window_size[0]}x{self.window_size[1]}")

        # Label
        sub_window_action_label = tk.Label(
            master=self.sub_window, text="Actions", font=("Fira Code", 20)
        )
        sub_window_action_label.pack()

        # Frame
        sub_window_action_frame = tk.Frame(master=self.sub_window)

        self.sub_window.bind(
            "<Control-1>",
            lambda e: self.add_action_widgets(sub_window_action_frame, e.x, e.y),
        )
        sub_window_action_frame.pack(anchor="center")

        sub_window_action_button_frame = tk.Frame(master=self.sub_window)

        # Button
        sub_window_action_cancel_button = tk.Button(
            master=sub_window_action_button_frame,
            text="Ok",
            font=("Fira Code", 20),
            command=lambda: self.sub_window_buttons_action(0, self.sub_window),
        )

        sub_window_action_ok_button = tk.Button(
            master=sub_window_action_button_frame,
            text="Cancel",
            font=("Fira Code", 20),
            command=lambda: self.sub_window_buttons_action(1, self.sub_window),
        )

        sub_window_action_cancel_button.pack(side="left", padx=20)
        sub_window_action_ok_button.pack(side="left", padx=20)

        sub_window_action_button_frame.pack(pady=20)


if __name__ == "__main__":
    ui = UI()
    console = Console()
    console.clear()
    console.print(Panel("👍 Hand Gesture Recognition"))

    ui.create_main_window("assets/Thumbs Up.png", "👍 HGR - Hand Gesture Recognizer")

    console.clear()
