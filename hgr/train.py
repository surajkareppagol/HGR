import mp.train
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

    window.update()

    train_dataset(window, dataset)

    # End Button
    ok_B = ttk.Button(master=window, text="Ok")
    ok_B.pack(pady=20)

    # Bind Button
    ok_B.bind("<1>", lambda _: window.destroy())


def train_dataset(window, dataset):
    train = mp.train.Train(dataset_path=dataset)
    train.split()

    # Train Label
    ttk.Label(
        master=window,
        text="🔀 Data Split Successfully.",
    ).pack()

    window.update()

    train.train()

    train.export()

    # End Label
    ttk.Label(
        master=window,
        text='📄 Task file "custom_model.task" exported.',
    ).pack()

    window.update()

    accuracy, loss = train.evaluate_model()

    ttk.Label(
        master=window,
        text=f"🎯 Evaluation Results: 📈 {round(accuracy, 2)}%, 📉 {round(loss, 2)}%.",
    ).pack()
