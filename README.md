# 👍 HGR - Hand Gesture Recognition

HGR is a hand gesture recognition system built with Google MediaPipe.

> 🚧 Under Development

## ⚙️ Usage

```sh
git clone https://github.com/surajkareppagol/HGR
cd HGR
```

```sh
python3 -m venv venv
```

```sh
source venv/bin/activate
```

```sh
pip install -r requirements.txt
```

```sh
python3 hgr/main.py
```

`deactivate` the virtual environment.

```sh
deactivate
```

## ✅ Requirements

- 🐍 Python3.7+
- ✨ mediapipe
- ✨ mediapipe-model-maker
- ⚡ rich
- 🌟 ttkbootstrap
- 🖱️ pyautogui

Mediapipe requires `Python` versions between `3.7` and `3.10`. In `Windows` there are some problems with mediapipe installation, so it is recommended to install these using `pip`.

Recent changes in tensorflow broke the model maker, so use the following to install `mediapipe-model-maker`.

```sh
pip install "keras<3.0.0" mediapipe-model-maker
```

## ↔️ API Class

The `hgr/mp/api.py` provides a `API Class`, that has following methods.

- `get_gestures()`

  Returns a list of available gestures.

- `get_landmarks_image()`

  Returns landmarks from a image passed as argument.

- `draw_landmarks_image()`

  Draws points on landmarks and connects them.

- `get_landmark_image()`

  Returns landmarks for a specific point, between 0 - 20.

  ![MediaPipe Hands](https://developers.google.com/static/mediapipe/images/solutions/hand-landmarks.png)

- `get_gesture_image()`

  Classifies the gesture from image, and returns it.

## 🖥️ GUI

![HGR Main](https://raw.githubusercontent.com/surajkareppagol/Assets/main/16%20-%20HGR/HGR%20Main.png)

![HGR Actions](https://raw.githubusercontent.com/surajkareppagol/Assets/main/16%20-%20HGR/HGR%20Actions.png)

![HGR Train](https://raw.githubusercontent.com/surajkareppagol/Assets/main/16%20-%20HGR/HGR%20Train.png)

![HGR Test](https://raw.githubusercontent.com/surajkareppagol/Assets/main/16%20-%20HGR/HGR%20Test.png)

## 🎯 Model Maker Scores

```txt
╔═══════════╤══════════╤════════════════════╗
║ Iteration │ Gesture  │       Score        ║
╟───────────┼──────────┼────────────────────╢
║     1     │   none   │ 0.8584573268890381 ║
║     2     │   none   │ 0.568006694316864  ║
║     3     │  paper   │ 0.9921259880065918 ║
║     4     │  paper   │ 0.991919994354248  ║
║     5     │  paper   │ 0.9897699356079102 ║
║     6     │  paper   │ 0.9981831908226013 ║
║     7     │  paper   │ 0.9804528951644897 ║
║     8     │   none   │ 0.893876314163208  ║
║     9     │  paper   │ 0.9854918122291565 ║
║    10     │   none   │ 0.8718634247779846 ║
║    11     │   none   │ 0.760579526424408  ║
║    12     │ scissors │ 0.5368748307228088 ║
║    13     │   none   │ 0.8792762160301208 ║
║    14     │   none   │ 0.7174986600875854 ║
║    15     │   none   │ 0.9842039942741394 ║
║    16     │   none   │ 0.9359919428825378 ║
║    17     │   none   │ 0.948810338973999  ║
║    18     │   none   │ 0.9333010911941528 ║
║    19     │  paper   │ 0.6957719326019287 ║
║    20     │ scissors │ 0.9800419211387634 ║
║    21     │ scissors │ 0.6627081036567688 ║
║    22     │ scissors │ 0.9795249104499817 ║
║    23     │ scissors │ 0.9814074039459229 ║
║    24     │ scissors │ 0.9789888858795166 ║
║    25     │   none   │ 0.9442585706710815 ║
║    26     │ scissors │ 0.959807276725769  ║
║    27     │   none   │ 0.9233239889144897 ║
║    28     │   none   │ 0.9254647493362427 ║
║    29     │  paper   │ 0.8687804937362671 ║
║    30     │  paper   │ 0.8441806435585022 ║
║    31     │          │ 0.8685176372528076 ║
║    32     │   none   │ 0.965121328830719  ║
║    33     │   none   │ 0.9680899977684021 ║
║    34     │ scissors │ 0.9052069187164307 ║
║    35     │ scissors │ 0.8518658876419067 ║
║    36     │ scissors │ 0.9516168236732483 ║
║    37     │ scissors │ 0.9168112874031067 ║
║    38     │ scissors │ 0.9222723245620728 ║
║    39     │ scissors │ 0.9808273315429688 ║
║    40     │ scissors │ 0.9677468538284302 ║
║    41     │   none   │ 0.8759973049163818 ║
║    42     │   none   │ 0.8951284885406494 ║
║    43     │   none   │ 0.5676480531692505 ║
║    44     │   none   │ 0.8585500717163086 ║
║    45     │   none   │ 0.9657561182975769 ║
║    46     │   none   │ 0.8343509435653687 ║
║    47     │   none   │ 0.8246175646781921 ║
║    48     │   none   │ 0.9299445152282715 ║
║    49     │   none   │ 0.9493988156318665 ║
║    50     │   rock   │ 0.6069502830505371 ║
║    51     │   none   │ 0.9981077909469604 ║
║    52     │   rock   │ 0.526486337184906  ║
║    53     │   none   │ 0.8241088390350342 ║
║    54     │   none   │ 0.547508180141449  ║
║    55     │   none   │ 0.7531124949455261 ║
║    56     │   none   │ 0.9233627915382385 ║
║    57     │   none   │ 0.9331709742546082 ║
╚═══════════╧══════════╧════════════════════╝
```
