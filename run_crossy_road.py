import time
import numpy as np
import cv2
from scipy import misc
import mss

import constants_crossy_road as const
import movement_crossy_road as move
import process_image_crossy_road as process_image
import process_input_crossy_road as process_input

# for i in range(5, 0, -1):
#     print(i)
#     time.sleep(1)

sct = mss.mss()

while(True):
    last_time = time.time()

    raw_img = np.array(sct.grab(const.MONITOR))

    game_over, processed_img, network_input = process_image.process(raw_img)

    processed_input = process_input.process(network_input, const.IRRELEVANT_INPUT)

    # print(game_over)
    # print(processed_input)
    cv2.imshow('Processed Image', processed_img)
    # Press "q" to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

    # move.forward()

    while(time.time()-last_time < const.MOVE_TIME):
        time.sleep(0.0001)

    # print('fps: {0}'.format(1 / (time.time()-last_time)))
