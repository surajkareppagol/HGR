from json import loads

import pyautogui


def get_actions():
    with open("logs/actions.json", "r") as file:
        actions_ = loads(file.read())
    return actions_


actions_ = get_actions()


def actions(gesture):
    print(actions_)
    if gesture in actions_.keys():
        x, y = actions_[gesture]["points"]

        pyautogui.moveTo(x, y)
        pyautogui.click()
