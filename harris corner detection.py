import cv2
import numpy as np

def detect_corners(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect corners using Harris Corner Detection
    dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

    # Dilate the detected corners to enhance visibility
    dst = cv2.dilate(dst, None)

    # Threshold the corner response
    threshold = 0.01 * dst.max()
    corner_image = np.zeros_like(image)
    corner_image[dst > threshold] = [0, 0, 255]  # Red color for detected corners

    # Display the original image and detected corners
    cv2.imshow('Original Image', image)
    cv2.imshow('Detected Corners', corner_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
# Detect corners in the image
detect_corners('C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg')
