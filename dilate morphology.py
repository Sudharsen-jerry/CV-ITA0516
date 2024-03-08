import cv2
import numpy as np
image = cv2.imread('C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg', 0) # Load image in grayscale
kernel = np.ones((5,5), np.uint8)
erosion = cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel)
dilation = cv2.morphologyEx(image, cv2.MORPH_DILATE, kernel)
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', erosion)
cv2.imshow('Dilated Image', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
