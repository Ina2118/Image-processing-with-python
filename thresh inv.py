import cv2
import numpy as np

# image path 
path = r'C:\Users\User\Desktop\irina\TI\segmentation\yes\segmentation\Yes 3.jpg'
img = cv2.imread(path)

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval,threshInv = cv2.threshold(grayscaled, 155, 255,cv2.THRESH_BINARY_INV)
cv2.imshow('original',img)
cv2.imshow('threshold',threshInv)
cv2.waitKey(0)
cv2.destroyAllWindows()