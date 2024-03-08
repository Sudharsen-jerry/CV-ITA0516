import cv2

# Full path of the image file
image_path = 'C:\\Users\\ADMIN\\Documents\\doctor.jpg'

# Read the image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the original and grayscale images
cv2.imshow('Original Image', image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
