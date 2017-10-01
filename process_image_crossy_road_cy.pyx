import cython
import cv2

@cython.boundscheck(False)
def binarify(img, int block_x, int block_y, 
        int [:,:] color_list_chicken,
        int [:,:] color_list_simple, int [:,:] color_list_tricky,
        chicken_num, floor_num, death_num):
    arr = []
    cdef int rows, cols, ch
    rows, cols, ch = img.shape

    cdef int x, y, i
    for y in range(block_x // 2, rows, block_x):
        for x in range(block_y // 2, cols, block_y):
            if(is_empty(x,y)): continue
            elif(is_thing(img,color_list_simple,x,y,block_x,block_y,1)):
                cv2.circle(img, (x, y), 3, [255, 0, 0], -1) 
                arr.append(floor_num)
            elif(is_thing(img,color_list_tricky,x,y,block_x,block_y,4)):
                cv2.circle(img, (x, y), 3, [255, 0, 0], -1) 
                arr.append(floor_num)
            elif(is_thing(img,color_list_chicken,x,y,block_x,block_y,4)):
                cv2.circle(img, (x, y), 5, [0, 255, 0], -1) 
                arr.append(chicken_num)
            else:
                cv2.circle(img, (x, y), 3, [0, 0, 255], -1) 
                arr.append(death_num)

    for i in range(1, cols // block_y + 1):
        cv2.line(img, (i * block_y, 0), (i * block_y, rows), (255, 0, 0), 1)
    for i in range(1, rows // block_x + 1):
        cv2.line(img, (0, i * block_x), (cols, i * block_x), (255, 0, 0), 1)

    return img, arr

@cython.boundscheck(False)
cdef bint is_thing(img, int[:,:] color_list, 
        int x, int y, int block_x, int block_y, int num):
    cdef unsigned char[:] pixel0, pixel1, pixel2, pixel3
    if(num == 1):
        if(is_thing_helper(img[y,x], color_list)):
            return True
    elif(num == 4):
        pixel0 = img[y][x + (block_x // 6)]
        pixel1 = img[y][x - (block_x // 6)]
        pixel2 = img[y + (block_y // 6)][x]
        pixel3 = img[y - (block_y // 6)][x]

        if(is_thing_helper(pixel0,color_list) or
                is_thing_helper(pixel1,color_list) or
                is_thing_helper(pixel2,color_list) or
                is_thing_helper(pixel3,color_list)): 
            return True

    return False

@cython.boundscheck(False)
cdef bint is_thing_helper(unsigned char[:] pixel, int[:,:] color_list):
    cdef int i
    for i in range(color_list.shape[0]):
        if(pixel[0] == color_list[i][0] and
                pixel[1] == color_list[i][1] and
                pixel[2] == color_list[i][2]):
            return True

    return False

@cython.boundscheck(False)
cdef bint is_empty(int x, int y):
    cdef float a = -0.3 * x + 63
    cdef float b = 2.05 * x + 50
    cdef float c = -0.28 * x + 537
    cdef float d = 2.05 * x - 480

    if(y < a): return True
    if(y > b): return True
    if(y > c): return True
    if(y < d): return True

    return False
