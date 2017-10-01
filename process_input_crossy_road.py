import numpy as np
import mss
import cv2

import process_image_crossy_road as process_image
import constants_crossy_road as const

def process(input_arr):
    try:
        idx = len(input_arr) - 1 - input_arr[::-1].index(const.CHICKEN)
        shift_amt = ((idx // 10)+1) % 2
        new_arr = (input_arr[idx+1-20-2:idx+1-20+3] + 
                   input_arr[idx+shift_amt-10-2:idx+shift_amt-10+3] +
                   input_arr[idx-2:idx] + input_arr[idx+1:idx+3])
        if(len(new_arr) != 14):
            new_arr = [const.DEATH] * 14
    except:
        new_arr = [const.DEATH] * 14
    
    return new_arr

if __name__ == '__main__':
    sct = mss.mss()

    while(True):
        raw_img = np.array(sct.grab(const.MONITOR))
        raw_img = raw_img[:, :, 0:3]

        _, processed_img, processed_arr = process_image.process(raw_img)

        processed_input = process(processed_arr)
        print(processed_input)

        cv2.imshow('Processed Image', processed_img)
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

