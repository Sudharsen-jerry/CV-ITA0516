import cv2
import numpy as np

# Load image
image = cv2.imread('C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg', 0) # Load image in grayscale

# Define kernel for morphology operations
kernel = np.ones((5,5), np.uint8)

# Apply erosion
erosion = cv2.morphologyEx(image, cv2.MORPH_ERODE, kernel)

# Apply dilation
dilation = cv2.morphologyEx(image, cv2.MORPH_DILATE, kernel)

# Display original, eroded, and dilated images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', erosion)
cv2.imshow('Dilated Image', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()
