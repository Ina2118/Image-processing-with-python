import numpy as np
import cv2
from matplotlib import pyplot as plt

# image path 
path = r'C:\Users\User\Desktop\irina\TI\segmentation\yes\segmentation\remove 1.png'

# using imread()  
img = cv2.imread(path)
dst = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

plt.subplot(121), plt.imshow(img)
plt.subplot(122), plt.imshow(dst)
plt.show()