import cython
import cv2

@cython.boundscheck(False)
def binarify(img, int block_x, int block_y, int [:,:] color_list):
    arr = []
    cdef int rows, cols, ch
    rows, cols, ch = img.shape

    cdef int x, y, i
    for y in range(block_x // 2, rows, block_x):
        for x in range(block_y // 2, cols, block_y):
            if(is_floor(img[y,x], color_list)):
                cv2.circle(img, (x, y), 5, [255, 0, 0], -1) 
                arr.append(1)
            else:
                cv2.circle(img, (x, y), 5, [0, 0, 255], -1) 
                arr.append(0)

    for i in range(1, cols // block_y + 1):
        cv2.line(img, (i * block_y, 0), (i * block_y, rows), (255, 0, 0), 1)
    for i in range(1, rows // block_x + 1):
        cv2.line(img, (0, i * block_x), (cols, i * block_x), (255, 0, 0), 1)

    return img, arr

@cython.boundscheck(False)
cdef bint is_floor(unsigned char[:] pixel, int[:,:] color_list):
    cdef unsigned char[:] pixel_color = pixel[:3] # pixel has 4 channels

    cdef int i
    for i in range(color_list.shape[0]):
        if(pixel_color[0] == color_list[i][0] and
                pixel_color[1] == color_list[i][1] and
                pixel_color[2] == color_list[i][2]):
            return True

    return False
