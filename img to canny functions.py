import cv2

# Full path of the image file
image_path = 'C:\\Users\\ADMIN\\Documents\\doctor.jpg'

# Read the image
image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray_image, 100, 200)  # Adjust threshold values as needed

# Display the original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Edge-detected Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
