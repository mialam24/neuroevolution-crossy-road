import pyautogui
import time
import numpy
import cv2
import subprocess
from scipy import misc

# Constants
DIM_X = 432
DIM_Y = 240
CLICK_X = DIM_X/2
CLICK_Y = DIM_Y/2

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

# pyautogui.click(CLICK_X, CLICK_Y, clicks=10000, interval=0.5)

while(True):
    last_time = time.time()

    subprocess.run("adb shell screencap -p | sed 's/\r$//' > screenshot.png", shell=True, check=True)
    raw_img = misc.imread('screenshot.png')

    # Display the picture
    # cv2.imshow('OpenCV/Numpy normal', img)
    # 
    # # Display the picture in grayscale
    cv2.imshow('OpenCV/Numpy grayscale',
            cv2.cvtColor(raw_img, cv2.COLOR_BGRA2GRAY))

    print('fps: {0}'.format(1 / (time.time()-last_time)))

    # Press "q" to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
