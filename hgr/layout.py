import tkinter as tk

import cv2 as cv
import ttkbootstrap as ttk
from PIL import Image, ImageTk


def add_tklabel(master, x=0, y=0):
    tk_label = tk.Label(master=master, text=f"({x}, {y})")
    tk_label.pack()


def open_cam():
    success, frame = cap.read()

    if success:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        image = Image.fromarray(frame)
        image = ImageTk.PhotoImage(image=image)

        cam_label.photo = image  # type: ignore

        cam_label.configure(image=image)

    root.after(20, open_cam)


def set_actions():
    actions_root = tk.Toplevel()
    actions_root.title("Actions")
    actions_root.geometry(f"{root_width}x{root_height}")
    actions_root.attributes("-alpha", 0.5)

    actions_label = tk.Label(
        master=actions_root, text="Actions", font=("Fira Code", 20)
    )
    actions_label.pack()

    actions_root.bind("<Button-1>", lambda e: add_tklabel(actions_root, e.x, e.y))


cap = cv.VideoCapture(0)

root = ttk.Window(themename="darkly", title="👍 HGR - Hand Gesture Recognizer")

root_width = root.winfo_screenwidth()
root_height = root.winfo_screenheight()

root.geometry(f"{root_width}x{root_height}")

cam_label = tk.Label(master=root, text="", anchor="center", pady=20)
cam_label.pack(fill="both", expand=True)

button_frame = tk.Frame(master=root, padx=20, pady=80)

start_button = tk.Button(master=button_frame, text="Start HGR", font=("Fira Code", 20))

end_button = tk.Button(master=button_frame, text="End HGR", font=("Fira Code", 20))

actions_button = tk.Button(
    master=button_frame, text="Set Actions", font=("Fira Code", 20), command=set_actions
)

train_button = tk.Button(
    master=button_frame, text="Train Model", font=("Fira Code", 20)
)

start_button.pack(side="left")
end_button.pack(side="left", padx=10)
actions_button.pack(side="left", padx=20)
train_button.pack(side="left", padx=10)

button_frame.pack()

end_button.bind("<Button-1>", lambda e: root.quit())

open_cam()

root.bind("<Escape>", lambda e: root.quit())

root.mainloop()

cap.release()
