import pyautogui
import time

import constants_crossy_road as const

dist = 0
score = 0

def forward():
    pyautogui.click(const.MID_X, const.MID_Y)

    global dist
    global score
    dist += 1
    score = max(score, dist)

def left():
    pyautogui.moveTo(const.MID_X, const.MID_Y)
    pyautogui.dragRel(-const.DRAG_OFFSET, 0, const.DRAG_TIME, button='left')

def right():
    pyautogui.moveTo(const.MID_X, const.MID_Y)
    pyautogui.dragRel(const.DRAG_OFFSET, 0, const.DRAG_TIME, button='left')

def backward():
    pyautogui.moveTo(const.MID_X, const.MID_Y)
    pyautogui.dragRel(0, const.DRAG_OFFSET, const.DRAG_TIME, button='left')

    global dist
    dist -= 1

def restart():
    pyautogui.click(x = const.PLAY_BUTTON_X, y = const.PLAY_BUTTON_Y)
    time.sleep(const.WAIT_SCREEN)
    forward()

    global dist
    global score 
    dist = 1
    score = 1

def get_score():
    return score
