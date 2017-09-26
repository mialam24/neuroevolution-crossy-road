import pyautogui
import time

import constants_crossy_road as const

dist = 0
score = 0

def forward():
    pyautogui.keyDown('up')
    time.sleep(const.PRESS_TIME)
    pyautogui.keyUp('up')

    global dist
    global score
    dist += 1
    score = max(score, dist)

def left():
    pyautogui.keyDown('left')
    time.sleep(const.PRESS_TIME)
    pyautogui.keyUp('left')

def right():
    pyautogui.keyDown('right')
    time.sleep(const.PRESS_TIME)
    pyautogui.keyUp('right')

def backward():
    pyautogui.keyDown('down')
    time.sleep(const.PRESS_TIME)
    pyautogui.keyUp('down')

    global dist
    dist -= 1

def restart():
    pyautogui.click(x = const.PLAY_BUTTON_X, y = const.PLAY_BUTTON_Y)
    time.sleep(const.WAIT_SCREEN)
    pyautogui.click(5 + const.X_OFFSET, -20 + const.DIM_Y + const.Y_OFFSET)

    global dist
    global score 
    dist = 1
    score = 1

def get_score():
    return score

if __name__ == '__main__':
    restart()
    start = time.time()
    left()
    right()
    backward()
    forward()
    end = time.time()
    print("Took", end-start, " seconds")
    print(get_score())
