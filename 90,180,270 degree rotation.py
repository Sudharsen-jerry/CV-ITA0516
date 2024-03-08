import cv2

# Load the image
image = cv2.imread('C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg')

# Rotate the image by 90 degrees
rotated_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Rotate the image by 180 degrees
rotated_180 = cv2.rotate(image, cv2.ROTATE_180)

# Rotate the image by 270 degrees
rotated_270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display the rotated images
cv2.imshow('Rotated 90', rotated_90)
cv2.imshow('Rotated 180', rotated_180)
cv2.imshow('Rotated 270', rotated_270)

cv2.waitKey(0)
cv2.destroyAllWindows()
