import cv2
import numpy as np
import mss

import constants_crossy_road as const
import process_image_crossy_road_cy as proc_cy

def process(img):
    rotated_img = rotate(img, const.ROTATION_ANGLE)
    affine_img = affine_transform(rotated_img)
    adj_img = adjust_size(affine_img, const.BLOCK_X, const.BLOCK_Y)
    shifted_img = shift_image(adj_img, -4, -10)

    bin_img, bin_arr = proc_cy.binarify(shifted_img, const.BLOCK_X, const.BLOCK_Y, const.COLOR_LIST_FLOOR)

    marked_img = mark_chicken(bin_img, const.BLOCK_X, const.BLOCK_Y, const.HOME_CELL_X, const.HOME_CELL_Y)

    return marked_img, bin_arr

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

def mark_chicken(img, block_x, block_y, home_x, home_y):
    mark_x = block_x * home_x + block_x // 2
    mark_y = block_y * home_y + block_y // 2

    marked_img = cv2.circle(img, (mark_x, mark_y), 5, [0, 255, 0], -1)

    return marked_img

if __name__ == '__main__':
    with mss.mss() as sct:
        raw_img = np.array(sct.grab(const.MONITOR))

    processed_img, processed_arr = process(raw_img)

    # print(processed_arr)
    cv2.imshow('Processed Image', processed_img)

    while(True):
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
