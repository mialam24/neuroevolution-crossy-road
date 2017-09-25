import cv2
import numpy as np

def rotate_and_scale(img_in, angle, scale):
    old_Y, old_X, ch = img_in.shape 
    M = cv2.getRotationMatrix2D((old_X/2,old_Y/2), angle, scale) 

    new_X, new_Y = old_X*scale,old_Y*scale
    r = np.deg2rad(angle)
    new_X, new_Y = (abs(np.sin(r)*new_Y) + abs(np.cos(r)*new_X),
            abs(np.sin(r)*new_X) + abs(np.cos(r)*new_Y))

    tx, ty = ((new_X-old_X)/2,(new_Y-old_Y)/2)
    M[0,2] += tx 
    M[1,2] += ty

    img_out = cv2.warpAffine(img_in, M, (int(new_X),int(new_Y)))

    return img_out


if __name__ == '__main__':
    img = cv2.imread('screenshot.png')
    rotated_img = rotate_and_scale(img, 15, 1)
    cv2.imshow('Processed Image', rotated_img)

    while(True):
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
