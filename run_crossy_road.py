import time
import numpy
import cv2
from scipy import misc
import mss

import constants_crossy_road as const
import movement_crossy_road as move
import process_image_crossy_road as process_image

MONITOR = {'top': const.Y_OFFSET, 'left': 0, 'width': const.DIM_X, 'height': const.DIM_Y}

for i in range(5, 0, -1):
    print(i)
    time.sleep(1)

sct = mss.mss()

while(True):
    last_time = time.time()

    raw_img = numpy.array(sct.grab(MONITOR))

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
