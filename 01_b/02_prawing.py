import cv2
import numpy as np

orginal_img = cv2.imread(filename=r'/01_b/assets/python.png')
img = orginal_img.copy()

height, width = img.shape[:2]
print(f'Wysokosc: {height}')
print(f'Szerokość: {width}')


cv2.line(img=img, pt1=(0, 0), pt2=(width,height), color=(0,0,255),thickness=5 )
cv2.imshow(winname='logo', mat=img)
cv2.waitKey(0)