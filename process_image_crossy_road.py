import cv2
import numpy as np
import mss

import constants_crossy_road as const
import process_image_crossy_road_cy as proc_cy

def process(img):
    game_status = is_game_over(img, const.PLAY_BUTTON_X - 10, const.PLAY_BUTTON_Y - const.Y_OFFSET, const.GAME_OVER_COLOR)

    rotated_img = rotate(img, const.ROTATION_ANGLE)
    affine_img = affine_transform(rotated_img)
    adj_img = adjust_size(affine_img, const.BLOCK_X, const.BLOCK_Y)
    shifted_img = shift_image(adj_img, -4, -10)

    bin_img, bin_arr = proc_cy.binarify(shifted_img, const.BLOCK_X, const.BLOCK_Y, const.COLOR_LIST_FLOOR, const.FLOOR, const.DEATH)
    
    return game_status, bin_img, bin_arr

def rotate(img, angle):
    old_Y, old_X, ch = img.shape 
    M = cv2.getRotationMatrix2D((old_X/2,old_Y/2), angle, 1) 

    r = np.deg2rad(angle)
    new_X, new_Y = (abs(np.sin(r)*old_Y) + abs(np.cos(r)*old_X),
            abs(np.sin(r)*old_X) + abs(np.cos(r)*old_Y))

    tx, ty = ((new_X-old_X)/2,(new_Y-old_Y)/2)
    M[0,2] += tx 
    M[1,2] += ty

    rotated_img = cv2.warpAffine(img, M, (int(new_X),int(new_Y)))

    return rotated_img

def affine_transform(img):
    rows,cols,ch = img.shape
    
    pts1 = np.float32([[236,345],[258,345],[232,363]])
    pts2 = np.float32([[232,345],[254,345],[232,363]])
    
    M = cv2.getAffineTransform(pts1,pts2)
    M[0,2] += 66
    
    img_out = cv2.warpAffine(img,M,(cols+78,rows))
    
    return img_out

def adjust_size(img, block_x, block_y):
    rows, cols, ch = img.shape

    rows_needed = block_y - (rows % block_y)
    cols_needed = block_x - (cols % block_x)

    resized_img = cv2.copyMakeBorder( img, rows_needed // 2, 
            -(-rows_needed // 2), cols_needed // 2, -(-cols_needed // 2), 
            cv2.BORDER_CONSTANT, value=[0, 0, 0])

    return resized_img

def shift_image(img, shift_x, shift_y):
    rows, cols, ch = img.shape
    M = np.float32([[1,0,shift_x],[0,1,shift_y]])
    shifted_img = cv2.warpAffine(img , M, (cols,rows))

    return shifted_img

def is_game_over(img, x, y, color):
    pixel = img[y,x]
    if(pixel[0] == color[0] and
            pixel[1] == color[1] and
            pixel[2] == color[2]):
        return True

    return False

if __name__ == '__main__':
    with mss.mss() as sct:
        raw_img = np.array(sct.grab(const.MONITOR))

    game_status, processed_img, processed_arr = process(raw_img)

    print(game_status)
    # print(processed_arr)
    cv2.imshow('Processed Image', processed_img)

    while(True):
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
