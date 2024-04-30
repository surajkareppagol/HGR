from json import dumps
from os import path
from tkinter import PhotoImage, filedialog, font

import ui.actions


def get_icon(file):
    return PhotoImage(file=file)


def get_dimensions(window):
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    return width, height


def set_image(parent, image):
    parent.photo = image
    parent.configure(image=image)


def set_font():
    default = font.nametofont("TkDefaultFont")
    default.config(family="Fira Code", size=20)


def action_buttons(window, reset=False):
    if reset:
        ui.actions.actions = {}

    with open("logs/actions.json", "w") as file:
        file.write(dumps(ui.actions.actions))

    ui.actions.widgets = 0
    window.destroy()


def get_path():
    dataset = filedialog.askdirectory()

    if not path.exists(dataset):
        return None
    else:
        return dataset
