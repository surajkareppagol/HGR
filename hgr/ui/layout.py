import tkinter as tk

import ttkbootstrap as ttk
from camera import set_detect
from train import train
from ui.actions import get_position, set_widget
from ui.util import action_buttons, get_icon

## Widgets

# Label  - L
# Entry  - E
# Button - B
# Frame  - F
# Window - W
# FileDialog - D


def layout_main(parent, size):
    global camera_L

    # Camera Label
    camera_L = tk.Label(master=parent, text="", anchor="center")
    camera_L.pack(pady=20, fill="both", expand=True)

    # Buttons Frame
    buttons_F = ttk.Frame(master=parent)
    buttons_F.pack(padx=20, pady=80)

    # Control Buttons
    start_B = ttk.Button(master=buttons_F, text="Start HGR")
    start_B.pack(side="left")

    end_B = ttk.Button(master=buttons_F, text="End HGR")
    end_B.pack(side="left", padx=10)

    actions_B = ttk.Button(master=buttons_F, text="Set Actions")
    actions_B.pack(side="left", padx=20)

    train_B = ttk.Button(master=buttons_F, text="Train Model")
    train_B.pack(side="left", padx=10)

    # Button Bindings
    start_B.bind("<1>", lambda _: set_detect(True))
    end_B.bind("<1>", lambda _: set_detect(False))
    actions_B.bind("<1>", lambda _: layout_actions(size))
    train_B.bind("<1>", lambda _: layout_train(size))


def layout_actions(size):
    # Actions Window
    actions_W = tk.Toplevel()

    actions_W.title("👍 HGR - Actions")
    actions_W.iconphoto(False, get_icon("assets/icon.png"))

    # Set Screen Size
    actions_W.geometry(f"{size[0]}x{size[1]}")

    # Screen Label
    ttk.Label(master=actions_W, text="Actions").pack(padx=20)

    actions_W.bind(
        "<Control-1>",
        lambda _: set_widget(actions_W, get_position()),
    )

    actions_W.bind(
        "<Shift-1>",
        lambda _: set_widget(actions_W),
    )

    # Buttons Frame
    buttons_F = ttk.Frame(master=actions_W)
    buttons_F.pack(side="bottom", pady=30)

    # Control Buttons
    ok_B = ttk.Button(master=buttons_F, text="Ok")
    ok_B.pack(side="left", padx=20)

    cancel_B = ttk.Button(master=buttons_F, text="Cancel")
    cancel_B.pack(side="left", padx=20)

    # Bind Buttons
    ok_B.bind("<1>", lambda _: action_buttons(actions_W))
    cancel_B.bind("<1>", lambda _: action_buttons(actions_W, reset=True))

    actions_W.mainloop()


def layout_train(size):
    # Train Window
    train_W = tk.Toplevel()

    train_W.title("👍 HGR - Train Model")
    train_W.iconphoto(False, get_icon("assets/icon.png"))

    # Set Screen Size
    train_W.geometry(f"{size[0]}x{size[1]}")

    # Screen Label
    ttk.Label(master=train_W, text="Train Model").pack(padx=20)

    # Buttons Frame
    buttons_F = ttk.Frame(master=train_W)
    buttons_F.pack(anchor="center", pady=40)

    # Variable
    file_var = ttk.StringVar()

    # File Entry, Button
    file_E = ttk.Entry(master=buttons_F, textvariable=file_var, font=("Fira Code", 15))
    file_E.pack(side="left", padx=40)

    file_B = ttk.Button(master=buttons_F, text="Ok")
    file_B.pack(side="left", padx=10)

    # File Browse
    browse_B = ttk.Button(master=buttons_F, text="Browse")
    browse_B.pack(side="left", padx=10)

    # Bind Buttons
    file_B.bind(
        "<1>",
        lambda _: train(train_W, dataset=file_var.get()),
    )
    browse_B.bind("<1>", lambda _: train(train_W, browse=True))

    train_W.mainloop()
