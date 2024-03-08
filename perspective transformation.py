import cv2
import numpy as np

def perspective_transform(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Define the coordinates of the original image and the desired warped image
    original_pts = np.float32([[50, 50], [200, 50], [50, 200], [200, 200]])  # Define the four corners of the original image
    warped_pts = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])  # Define the four corners of the desired warped image

    # Calculate the perspective transformation matrix
    perspective_matrix = cv2.getPerspectiveTransform(original_pts, warped_pts)

    # Perform the perspective transformation
    warped_image = cv2.warpPerspective(image, perspective_matrix, (300, 300))

    # Display the original and warped images
    cv2.imshow('Original Image', image)
    cv2.imshow('Warped Image', warped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
# Perform a perspective transformation on the image
perspective_transform('C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg')
