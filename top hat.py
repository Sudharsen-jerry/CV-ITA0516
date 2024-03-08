import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg', cv2.IMREAD_GRAYSCALE)

# Define the structuring element (kernel)
kernel_size = (5, 5)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)

# Perform the opening operation
opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

# Calculate the Top Hat
tophat = cv2.subtract(image, opening)

# Display the original image and the Top Hat result
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(tophat, cmap='gray')
plt.title('Top Hat Result')

plt.show()
