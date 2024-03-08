import cv2

# Full path of the image file
image_path = 'C:\\Users\\ADMIN\\Documents\\doctor.jpg'

# Read the image
image = cv2.imread(image_path)

# Apply Gaussian blur
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)  # Adjust kernel size as needed

# Display the original and blurred images
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
