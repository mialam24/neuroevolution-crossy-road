import pyautogui
import time

import constants_crossy_road as const

pyautogui.PAUSE = const.PY_PAUSE

last_move_time = 0

def forward():
    global last_move_time
    time_since_last_move = time.time() - last_move_time
    if(time_since_last_move >= const.MOVE_TIME):
        pyautogui.keyDown('up')
        time.sleep(const.PRESS_TIME)
        pyautogui.keyUp('up')
        last_move_time = time.time()

def left():
    global last_move_time
    time_since_last_move = time.time() - last_move_time
    if(time_since_last_move >= const.MOVE_TIME):
        pyautogui.keyDown('left')
        time.sleep(const.PRESS_TIME)
        pyautogui.keyUp('left')
        last_move_time = time.time()

def right():
    global last_move_time
    time_since_last_move = time.time() - last_move_time
    if(time_since_last_move >= const.MOVE_TIME):
        pyautogui.keyDown('right')
        time.sleep(const.PRESS_TIME)
        pyautogui.keyUp('right')
        last_move_time = time.time()

def backward():
    global last_move_time
    time_since_last_move = time.time() - last_move_time
    if(time_since_last_move >= const.MOVE_TIME):
        pyautogui.click(x = const.PLAY_BUTTON_X, y = const.PLAY_BUTTON_Y)
        pyautogui.keyDown('down')
        time.sleep(const.PRESS_TIME)
        pyautogui.keyUp('down')
        last_move_time = time.time()

def restart():
    pyautogui.click(x = const.PLAY_BUTTON_X, y = const.PLAY_BUTTON_Y)
    time.sleep(const.WAIT_SCREEN)
    forward()

def escape():
    pyautogui.keyDown('esc')
    time.sleep(const.PRESS_TIME)
    pyautogui.keyUp('esc')
    time.sleep(const.WAIT_SCREEN)

if __name__ == '__main__':
    restart()
    start = time.time()
    left()
    right()
    backward()
    forward()
    end = time.time()
    print("Took", end-start, " seconds")
