import cv2
import numpy as np
import mss

import constants_crossy_road as const

num_0 = cv2.imread('digit-pngs/num_0.png')
num_1 = cv2.imread('digit-pngs/num_1.png')
num_2 = cv2.imread('digit-pngs/num_2.png')
num_3 = cv2.imread('digit-pngs/num_3.png')
num_4 = cv2.imread('digit-pngs/num_4.png')
num_5 = cv2.imread('digit-pngs/num_5.png')
num_6 = cv2.imread('digit-pngs/num_6.png')
num_7 = cv2.imread('digit-pngs/num_7.png')
num_8 = cv2.imread('digit-pngs/num_8.png')
num_9 = cv2.imread('digit-pngs/num_9.png')

num2_0 = cv2.imread('digit-pngs/num2_0.png')
num2_1 = cv2.imread('digit-pngs/num2_1.png')
num2_2 = cv2.imread('digit-pngs/num2_2.png')
num2_3 = cv2.imread('digit-pngs/num2_3.png')
num2_4 = cv2.imread('digit-pngs/num2_4.png')
num2_5 = cv2.imread('digit-pngs/num2_5.png')
num2_6 = cv2.imread('digit-pngs/num2_6.png')
num2_7 = cv2.imread('digit-pngs/num2_7.png')
num2_8 = cv2.imread('digit-pngs/num2_8.png')
num2_9 = cv2.imread('digit-pngs/num2_9.png')

num3_0 = cv2.imread('digit-pngs/num3_0.png')
num3_1 = cv2.imread('digit-pngs/num3_1.png')
num3_2 = cv2.imread('digit-pngs/num3_2.png')
num3_3 = cv2.imread('digit-pngs/num3_3.png')
num3_4 = cv2.imread('digit-pngs/num3_4.png')
num3_5 = cv2.imread('digit-pngs/num3_5.png')
num3_6 = cv2.imread('digit-pngs/num3_6.png')
num3_7 = cv2.imread('digit-pngs/num3_7.png')
num3_8 = cv2.imread('digit-pngs/num3_8.png')
num3_9 = cv2.imread('digit-pngs/num3_9.png')

def get_score():
    num_arr = []
    shift_x = 0
    
    while(True):
        digit_capture = {'top': const.DIGIT_Y + const.Y_OFFSET, 
                'left': const.DIGIT_X + const.X_OFFSET + shift_x, 
                'width': const.DIGIT_WIDTH, 
                'height': const.DIGIT_HEIGHT}

        with mss.mss() as sct:
            raw_img = np.array(sct.grab(digit_capture))

        raw_img = raw_img[:, :, 0:3]
        raw_img[np.where((raw_img!=[255,0,0]).all(axis=2))] = [0,0,0]
        raw_img[np.where((raw_img!=[0,255,0]).all(axis=2))] = [0,0,0]
        raw_img[np.where((raw_img!=[0,0,255]).all(axis=2))] = [0,0,0]

        if not num_arr:
            num = identify_digit(raw_img, -1)
        else: 
            num = identify_digit(raw_img, num_arr[-1])

        if(num == -1): break
        elif(num == 1): shift_x += const.DIGIT_WIDTH_ONE - 3
        else: shift_x += const.DIGIT_WIDTH - 3
        num_arr.append(num)

    score = ''.join(str(e) for e in num_arr)
    score = int(score)
    return score

def identify_digit(img, prev_num):
    if(prev_num == -1):
        if(np.array_equal(img, num_0)): return 0
        if(np.array_equal(img[:,0:const.DIGIT_WIDTH_ONE], num_1)): return 1
        if(np.array_equal(img, num_2)): return 2
        if(np.array_equal(img, num_3)): return 3
        if(np.array_equal(img, num_4)): return 4
        if(np.array_equal(img, num_5)): return 5
        if(np.array_equal(img, num_6)): return 6
        if(np.array_equal(img, num_7)): return 7
        if(np.array_equal(img, num_8)): return 8
        if(np.array_equal(img, num_9)): return 9
    elif(prev_num != 1):
        if(np.array_equal(img, num3_0)): return 0
        if(np.array_equal(img[:,0:const.DIGIT_WIDTH_ONE], num3_1)): return 1
        if(np.array_equal(img, num3_2)): return 2
        if(np.array_equal(img, num3_3)): return 3
        if(np.array_equal(img, num3_4)): return 4
        if(np.array_equal(img, num3_5)): return 5
        if(np.array_equal(img, num3_6)): return 6
        if(np.array_equal(img, num3_7)): return 7
        if(np.array_equal(img, num3_8)): return 8
        if(np.array_equal(img, num3_9)): return 9
    else:
        if(np.array_equal(img, num2_0)): return 0
        if(np.array_equal(img[:,0:const.DIGIT_WIDTH_ONE], num2_1)): return 1
        if(np.array_equal(img, num2_2)): return 2
        if(np.array_equal(img, num2_3)): return 3
        if(np.array_equal(img, num2_4)): return 4
        if(np.array_equal(img, num2_5)): return 5
        if(np.array_equal(img, num2_6)): return 6
        if(np.array_equal(img, num2_7)): return 7
        if(np.array_equal(img, num2_8)): return 8
        if(np.array_equal(img, num2_9)): return 9
    return -1

if __name__ == '__main__':
    score = get_score()
    print(score)
