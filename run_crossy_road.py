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
    raw_img = np.array(sct.grab(MONITOR))

    last_time = time.time()

    rotated_img = process_image.rotate(raw_img, const.ROTATION_ANGLE)
    affine_img = process_image.affine_transform(rotated_img)

    rows, cols, ch = affine_img.shape

    for i in range(1, cols // 26 + 1):
        cv2.line(affine_img, (i * 26 - 4, 0), (i * 26 - 4, rows), (255, 0, 0), 1)
    for i in range(1, rows // 26 + 1):
        cv2.line(affine_img, (0, i * 26), (cols, i * 26), (255, 0, 0), 1)

    cv2.imshow('Processed Image', affine_img)

    # Press "q" to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

    # while(time.time()-last_time < 1./60):
    #     time.sleep(0.0001)

    print('fps: {0}'.format(1 / (time.time()-last_time)))
