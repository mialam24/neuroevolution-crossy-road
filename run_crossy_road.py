import time
import numpy as np
import cv2
from scipy import misc
import mss
import random

import constants_crossy_road as const
import movement_crossy_road as move
import process_image_crossy_road as process_image
import process_input_crossy_road as process_input
import score_crossy_road as score

sct = mss.mss()

while(True):
    raw_img = np.array(sct.grab(const.MONITOR))
    raw_img = raw_img[:, :, 0:3]
    _, processed_img, _ = process_image.process(raw_img)
    cv2.imshow('Processed Image', processed_img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

for generation in range(const.NUM_GENERATIONS):
    print("Generation: ", generation)
    for individual in range(const.NUM_INDIVIDUALS):
        print("Individual: ", individual)
        move.restart()

        while(True):
            last_time = time.time()
        
            raw_img = np.array(sct.grab(const.MONITOR))
        
            game_over, processed_img, network_input = process_image.process(raw_img)
            if(game_over):
                break
        
            processed_input = process_input.process(network_input, const.IRRELEVANT_INPUT)
        
            # print(game_over)
            # print(processed_input)
            cv2.imshow('Processed Image', processed_img)
            # Press "q" to quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                quit()
        
            rand_num = random.randint(0,8)
            if(rand_num == 0 or rand_num == 5 or rand_num == 6 or rand_num == 7):
                move.forward()
            elif(rand_num == 1):
                move.left()
            elif(rand_num == 2):
                move.right()
            elif(rand_num == 3):
                move.backward()
            elif(rand_num == 4):
                pass
        
            while(time.time()-last_time < const.MOVE_TIME):
                time.sleep(0.0001)
        
            # print('fps: {0}'.format(1 / (time.time()-last_time)))
        raw_img = np.array(sct.grab(const.MONITOR))
        print(score.get_score())
