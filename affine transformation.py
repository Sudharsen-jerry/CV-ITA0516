import cv2
import numpy as np

def affine_transform(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Define the transformation matrix
    # Example: rotating the image by 30 degrees and scaling by 0.5
    angle = 30
    scale = 0.5
    center = (image.shape[1] // 2, image.shape[0] // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    # Perform the affine transformation
    transformed_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

    # Display the original and transformed images
    cv2.imshow('Original Image', image)
    cv2.imshow('Transformed Image', transformed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
# Perform an affine transformation on the image
affine_transform('C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg')
