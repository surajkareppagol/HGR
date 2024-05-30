import os
from json import loads
from subprocess import run
from time import sleep

import alsaaudio
import pyautogui

current_brightness = 1.0
current_volume = 100

current_os = os.name


def get_actions():
    with open("logs/actions.json", "r") as file:
        actions_ = loads(file.read())
    return actions_


actions_ = get_actions()


def set_brightness():
    global current_brightness

    if current_brightness < 0.4:
        current_brightness = 1.0
    else:
        current_brightness -= 0.01

    run(["xrandr", "--output", "eDP-1", "--brightness", str(current_brightness)])


def set_volume():
    global current_volume

    if current_volume < 10:
        current_volume = 100
    else:
        current_volume -= 5

    mixer = alsaaudio.Mixer()
    mixer.setvolume(current_volume)


def actions(gesture):
    # print(gesture)
    if gesture in actions_.keys():
        x, y = actions_[gesture]["points"]

        command = actions_[gesture]["command"]

        if current_os == "posix":
            if command == "brightness":
                set_brightness()
            elif command == "volume":
                set_volume()
            elif "key" in command:
                key = command.split(" ")[-1]
                pyautogui.press(key)
            elif "open" in command:
                directory = command.split(" ")[-1].strip()
                run(["nemo", directory], shell=True)
            elif "type" in command:
                word = command.split(" ")[1:]
                pyautogui.write(word)
            else:
                command = run(command.split(" "), capture_output=True, shell=True)
                output = str(command.stdout, encoding="utf-8").strip()

                print(output)

        elif current_os == "nt":
            pass
        elif current_os == "mac":
            pass

        if x == -10 and y == -10:
            return

        pyautogui.moveTo(x, y)
        pyautogui.click()
        # sleep(10)
