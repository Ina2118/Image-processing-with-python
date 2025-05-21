import cv2
import numpy 
import numpy as np
  
# image path 
path = r'C:\Users\User\Desktop\irina\TI\segmentation\yes\segmentation\Yes 1.jpg'

# using imread()  
img = cv2.imread(path)

dst = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow('image', numpy.hstack((img, dst)))

cv2.waitKey(0);
cv2.destroyAllWindows();
cv2.waitKey(1)
