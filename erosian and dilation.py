import cv2
import numpy as np

# image path 
path = r'C:\Users\User\Desktop\irina\TI\segmentation\yes\segmentation\threshold1.png'

img = cv2.imread(path)

kernel = np.ones((5,5), np.uint8)

img_erosion = cv2.erode(img, kernel, iterations=4)
img_dilation = cv2.dilate(img, kernel, iterations=4)

cv2.imshow('Input', img)
cv2.imshow('Erosion', img_erosion)
cv2.imshow('Dilation', img_dilation)

cv2.waitKey(0)