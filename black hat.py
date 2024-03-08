import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg', cv2.IMREAD_GRAYSCALE)

# Define the structuring element (kernel)
kernel_size = (5, 5)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)

# Perform the closing operation
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Calculate the Black Hat
blackhat = cv2.subtract(closing, image)

# Display the original image and the Black Hat result
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

plt.subplot(1, 2, 2)
plt.imshow(blackhat, cmap='gray')
plt.title('Black Hat Result')

plt.show()
