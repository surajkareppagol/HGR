import tkinter as tk
from curses import panel
from tkinter import font, ttk

import cv2 as cv
from custom_gestures_train import Custom_Gestures_Train
from PIL import Image, ImageTk
from rich.console import Console
from rich.panel import Panel

console = Console()
console.clear()
console.print(Panel("👍 Hand Gesture Recognition"))


capture = cv.VideoCapture(0)

width, height = 800, 600


capture.set(cv.CAP_PROP_FRAME_WIDTH, width)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, height)

window = tk.Tk()
window.title("HGR")
window.geometry("800x600")

window.bind("<Escape>", lambda event: window.quit())

label = tk.Label(master=window)
label.pack()


def open_cam():
    _, frame = capture.read()

    image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
    captured = Image.fromarray(image)
    photo_image = ImageTk.PhotoImage(image=captured)

    label.photo_image = photo_image

    label.configure(image=photo_image)

    label.after(10, open_cam)


def train_data(dataset="data/Rock-Paper-Scissors-Data"):
    train = Custom_Gestures_Train(dataset)
    train.train(export_to="tasks")
    print("Training Done.")
    train.export(task="custom_model.task")
    print("Exported.")


button = tk.Button(master=window, text="Start", font=("0xProto", 20), command=open_cam)
button.pack()

button_train = tk.Button(
    master=window, text="Train", font=("0xProto", 20), command=train_data
)
button_train.pack()


window.mainloop()
