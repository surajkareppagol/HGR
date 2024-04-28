import tkinter as tk

import pyautogui
import ttkbootstrap as ttk

## Widgets

# Label  - L
# Entry  - E
# Button - B
# Frame  - F
# Window - W

actions = {}
widgets = 0


def add_action(points=(-10, -10), gesture="none", command=":"):
    if gesture not in actions.keys():
        actions[gesture] = {
            "points": points,
            "command": command,
        }

    actions[gesture]["points"] = points
    actions[gesture]["command"] = command


def get_position():
    position = pyautogui.position()
    return (position.x, position.y)


def set_widget(parent, size=(-10, -10)):
    global widgets

    if widgets >= 8:
        return

    position = size

    widgets += 1

    # Label And Buttons Frame
    widget_F = ttk.Frame(master=parent)
    widget_F.pack(pady=10, anchor="center")

    # Frame Labels
    tk.Label(
        master=widget_F,
        text=f"({position[0]}, {position[1]})",
        width=20,
    ).pack(side="left", padx=40, expand=True, fill="both")

    # Variables
    gesture_var = ttk.StringVar()
    command_var = ttk.StringVar()

    ## Gesture Frame
    gesture_F = ttk.Frame(master=widget_F)
    gesture_F.pack(side="left")

    # Gesture Entry, Buttons
    gesture_E = ttk.Entry(
        master=gesture_F,
        textvariable=gesture_var,
        font=("Fira Code", 15),
    )
    gesture_E.pack(side="left", padx=10)

    gesture_B = ttk.Button(master=gesture_F, text="Add")
    gesture_B.pack(side="left", padx=20)

    ## command Frame
    command_F = ttk.Frame(master=widget_F)
    command_F.pack(side="left")

    # command Entry, Buttons
    command_E = ttk.Entry(
        master=command_F,
        textvariable=command_var,
        font=("Fira Code", 15),
    )
    command_E.pack(side="left", padx=10)

    command_B = ttk.Button(master=command_F, text="Add")
    command_B.pack(side="left", padx=20)

    # Bind Buttons
    gesture_B.bind(
        "<1>",
        lambda _: add_action(position, gesture=gesture_var.get()),
    )

    command_B.bind(
        "<1>",
        lambda _: add_action(
            position, gesture=gesture_var.get(), command=command_var.get()
        ),
    )
