import tkinter as tk

import customtkinter as ctk
import cv2 as cv

# from custom_gestures_train import Custom_Gestures_Train
from PIL import Image, ImageTk

capture = cv.VideoCapture(0)


window = ctk.CTk()
window.title("HGR")
window.attributes("-fullscreen", True)

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

capture.set(cv.CAP_PROP_FRAME_WIDTH, width - 400)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, height - 400)


window.bind("<Escape>", lambda e: window.quit())

label = ctk.CTkLabel(master=window, text="")
label.pack()


def open_cam():
    _, frame = capture.read()

    converted_image = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
    captured_image = Image.fromarray(converted_image)
    ctk_image = ctk.CTkImage(
        light_image=captured_image,
        dark_image=captured_image,
        size=(width - 200, height - 200),
    )

    # label.photo_image = photo_image

    label.configure(image=ctk_image)

    label.after(10, open_cam)


# def train_data(dataset="data/Rock-Paper-Scissors-Data"):
#     train = Custom_Gestures_Train(dataset)
#     train.train(export_to="tasks")
#     print("Training Done.")
#     train.export(task="custom_model.task")
#     print("Exported.")

open_cam()

frame_buttons = ctk.CTkFrame(window)

button_train = ctk.CTkButton(frame_buttons, text="Train", font=("0xproto", 20))
button_train.pack()

print(button_train.__dir__())

button_actions = ctk.CTkButton(frame_buttons, text="Actions", font=("0xproto", 20))
button_actions.pack()
frame_buttons.pack()


window.mainloop()
