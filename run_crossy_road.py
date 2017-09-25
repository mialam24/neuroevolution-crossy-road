import time
import numpy as np
import cv2
from scipy import misc
import mss

import constants_crossy_road as const
import movement_crossy_road as move
import process_image_crossy_road as process_image

MONITOR = {'top': const.Y_OFFSET, 'left': 0, 'width': const.DIM_X, 'height': const.DIM_Y}

# for i in range(5, 0, -1):
#     print(i)
#     time.sleep(1)

sct = mss.mss()

while(True):
    last_time = time.time()

    raw_img = np.array(sct.grab(MONITOR))

    rotated_img = process_image.rotate_and_scale(raw_img, const.ROTATION_ANGLE, const.SCALE_FACTOR)

    cv2.imshow('Processed Image', rotated_img)

    print('fps: {0}'.format(1 / (time.time()-last_time)))

    # Press "q" to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
