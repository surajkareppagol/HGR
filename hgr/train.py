from time import sleep

import ttkbootstrap as ttk
from ui.util import get_path


def train(window, dataset="", browse=False):
    if browse:
        dataset = get_path()

    # Dataset Label
    ttk.Label(
        master=window,
        text=f'🔄 Training with dataset at, 📁 "{dataset}".',
    ).pack(pady=20)

    sleep(4)

    # End Label
    ttk.Label(
        master=window,
        text='📄 Task file "custom_model.task" exported.',
    ).pack()

    ttk.Label(master=window, text=f"🎯 Evaluation Results: 📈 {10}%, 📉 {10}%.").pack()

    # End Button
    ok_B = ttk.Button(master=window, text="Ok")
    ok_B.pack(pady=20)

    # Bind Button
    ok_B.bind("<1>", lambda _: window.destroy())
