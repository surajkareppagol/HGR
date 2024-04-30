from tkinter import PhotoImage, font

import ttkbootstrap as ttk

root = ttk.Window(themename="darkly")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

default = font.nametofont("TkDefaultFont")
default.config(family="Fira Code", size=20)

root.title("👍 HGR - Test App")
root.geometry(f"{width}x{height}")

root.iconphoto(False, PhotoImage(file="assets/construction.png"))


def set_color(widget, bg, fg="White"):
    widget.config(background=f"{bg}", foreground=f"{fg}")


def create_layout():
    # Root Frame
    root_F = ttk.Frame(master=root)
    root_F.pack(anchor="center", pady=200)

    # Left Frame
    left_F = ttk.Frame(master=root_F)
    left_F.pack(side="left")

    # Left Buttons
    white_B = ttk.Button(master=left_F, text="White", width=10)
    white_B.pack(pady=20)

    red_B = ttk.Button(master=left_F, text="Red", width=10)
    red_B.pack(pady=20)

    blue_B = ttk.Button(master=left_F, text="Blue", width=10)
    blue_B.pack(pady=20)

    # Center Label
    center_L = ttk.Label(
        master=root_F, text="    👍 HGR - Test App    ", background="Red"
    )
    center_L.pack(side="left", padx=100)

    # Right Frame
    right_F = ttk.Frame(master=root_F)
    right_F.pack(side="left")

    # Right Buttons
    green_B = ttk.Button(master=right_F, text="Green", width=10)
    green_B.pack(pady=20)

    yellow_B = ttk.Button(master=right_F, text="Yellow", width=10)
    yellow_B.pack(pady=20)

    orange_B = ttk.Button(master=right_F, text="Orange", width=10)
    orange_B.pack(pady=20)

    # Bind Buttons
    white_B.bind("<1>", lambda _: set_color(center_L, "white", "Black"))
    red_B.bind("<1>", lambda _: set_color(center_L, "Red"))
    blue_B.bind("<1>", lambda _: set_color(center_L, "Blue"))

    green_B.bind("<1>", lambda _: set_color(center_L, "Green"))
    yellow_B.bind("<1>", lambda _: set_color(center_L, "Yellow", "Black"))
    orange_B.bind("<1>", lambda _: set_color(center_L, "Orange"))


create_layout()

root.bind("<Escape>", lambda _: root.quit())

root.mainloop()
