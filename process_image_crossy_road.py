import cv2
import numpy as np

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

if __name__ == '__main__':
    img = cv2.imread('screenshot.png')
    rotated_img = rotate(img, 15)
    affine_img = affine_transform(rotated_img)

    rows, cols, ch = affine_img.shape

    for i in range(1, cols // 26 + 1):
        cv2.line(affine_img, (i * 26 - 4, 0), (i * 26 - 4, rows), (255, 0, 0), 1)
    for i in range(1, rows // 26 + 1):
        cv2.line(affine_img, (0, i * 26), (cols, i * 26), (255, 0, 0), 1)

    cv2.imshow('Processed Image', affine_img)

    while(True):
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
