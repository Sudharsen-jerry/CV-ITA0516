import cv2
import numpy as np

def sobel_edge_detection(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Sobel edge detection
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Combine the results
    sobel_combined = cv2.addWeighted(cv2.convertScaleAbs(sobel_x), 0.5, cv2.convertScaleAbs(sobel_y), 0.5, 0)

    # Display the original image and the Sobel edge detection result
    cv2.imshow('Original Image', image)
    cv2.imshow('Sobel Edge Detection', sobel_combined)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
# Apply Sobel edge detection on the image
sobel_edge_detection('C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg')
