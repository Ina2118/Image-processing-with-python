import numpy as np
import cv2
import cv2 as cv
from matplotlib import pyplot as plt

# image path 
path = r'C:\Users\User\Desktop\irina\TI\segmentation\yes\segmentation\5.png'

img = cv2.imread(path)

edges = cv.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()