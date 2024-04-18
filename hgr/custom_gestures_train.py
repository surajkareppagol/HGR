from os import listdir
from os.path import isdir, join

import matplotlib.pyplot as plt
from mediapipe_model_maker import gesture_recognizer


class Custom_Gestures_Train:
    def __init__(self, dataset_path=""):
        # "data/Rock-Paper-Scissors-Data"
        self.dataset_path = dataset_path
        self.labels = []
        self.NUM_EXAMPLES = 5
        self.model = None

        self.train_data = None
        self.rest_data = None
        self.validation_data = None
        self.test_data = None

    def print_labels(self):
        for i in listdir(self.dataset_path):
            if isdir(join(self.dataset_path, i)):
                self.labels.append(i)
        print(self.labels)

    def print_samples(self):
        for label in self.labels:
            label_dir = join(self.dataset_path, label)
            example_filenames = listdir(label_dir)[: self.NUM_EXAMPLES]
            fig, axs = plt.subplots(1, self.NUM_EXAMPLES, figsize=(10, 2))
            for i in range(self.NUM_EXAMPLES):
                axs[i].imshow(plt.imread(join(label_dir, example_filenames[i])))
                axs[i].get_xaxis().set_visible(False)
                axs[i].get_yaxis().set_visible(False)
            fig.suptitle(f"Showing {self.NUM_EXAMPLES} examples for {label}")

        plt.show()

    def train(self, export_to):
        data = gesture_recognizer.Dataset.from_folder(
            dirname=self.dataset_path,
            hparams=gesture_recognizer.HandDataPreprocessingParams(),
        )
        self.train_data, self.rest_data = data.split(0.8)
        self.validation_data, self.test_data = self.rest_data.split(0.5)

        print("Data split successfully")

        hparams = gesture_recognizer.HParams(export_dir=export_to)
        options = gesture_recognizer.GestureRecognizerOptions(hparams=hparams)
        self.model = gesture_recognizer.GestureRecognizer.create(
            train_data=self.train_data,
            validation_data=self.validation_data,
            options=options,
        )

    def evaluate_model(self):
        loss, acc = self.model.evaluate(self.test_data, batch_size=1)
        print(f"Test loss:{loss}, Test accuracy:{acc}")

    def export(self, task):
        self.model.export_model(task)
