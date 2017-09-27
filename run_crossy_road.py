import time
import numpy as np
import cv2
from scipy import misc
import mss
import random

import constants_crossy_road as const
import movement_crossy_road as move
import process_image_crossy_road as process_image
import score_crossy_road as score

sct = mss.mss()

while(True):
    last_time = time.time()

    raw_img = np.array(sct.grab(const.MONITOR))
    raw_img = raw_img[:, :, 0:3]
    _, processed_img, _ = process_image.process(raw_img)
    
    # print('fps: {0}'.format(1 / (time.time()-last_time)))

    cv2.imshow('Processed Image', processed_img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

for generation in range(1, const.NUM_GENERATIONS + 1):
    print("Generation: ", generation)
    for individual in range(1, const.NUM_INDIVIDUALS + 1):
        print("Individual: ", individual)
        move.restart()

        while(True):
            last_time = time.time()
        
            raw_img = np.array(sct.grab(const.MONITOR))
            raw_img = raw_img[:, :, 0:3]
        
            game_status, processed_img, network_input = process_image.process(raw_img)
            if(game_status == const.GAME_STATUS_GAME_OVER):
                break
            elif(game_status == const.GAME_STATUS_GREAT_SCORE):
                move.escape()
                break

            move.forward()
        
            cv2.imshow('Processed Image', processed_img)
            # Press "q" to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                quit()
        
            # print('fps: {0}'.format(1 / (time.time()-last_time)))
        
            # while(time.time()-last_time < const.MOVE_TIME):
            #     time.sleep(0.0001)

        print("Score", score.get_score())
