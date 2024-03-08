import cv2

# Read the image
image_path = 'C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg'
image = cv2.imread(image_path)

# Define the kernel for erosion
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # Adjust kernel size as needed

# Perform erosion
eroded_image = cv2.erode(image, kernel, iterations=1)  # Adjust iterations as needed

# Display the original and eroded images
cv2.imshow('Original Image', image)
cv2.imshow('Eroded Image', eroded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
