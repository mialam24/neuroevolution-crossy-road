import pyautogui
import time

import constants_crossy_road as const

pyautogui.PAUSE = const.PY_PAUSE

def forward():
    pyautogui.keyDown('up')
    time.sleep(const.PRESS_TIME)
    pyautogui.keyUp('up')

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

def restart():
    pyautogui.click(x = const.PLAY_BUTTON_X, y = const.PLAY_BUTTON_Y)
    time.sleep(const.WAIT_SCREEN)
    forward()

if __name__ == '__main__':
    restart()
    start = time.time()
    left()
    right()
    backward()
    forward()
    end = time.time()
    print("Took", end-start, " seconds")
