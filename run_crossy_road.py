import time
import numpy as np
import cv2
from scipy import misc
import mss

import constants_crossy_road as const
import movement_crossy_road as move
import process_image_crossy_road as process_image

# for i in range(5, 0, -1):
#     print(i)
#     time.sleep(1)

sct = mss.mss()

while(True):
    raw_img = np.array(sct.grab(const.MONITOR))

    last_time = time.time()

    processed_img, network_input = process_image.process(raw_img)

    # print(network_input)
    cv2.imshow('Processed Image', processed_img)
    # Press "q" to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

    while(time.time()-last_time < const.PRESS_TIME):
        time.sleep(0.0001)

    # print('fps: {0}'.format(1 / (time.time()-last_time)))
