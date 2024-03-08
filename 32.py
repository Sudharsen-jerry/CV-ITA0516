import numpy as np
import cv2

def create_colored_boxes(size):
    # Create a white image
    image = np.ones((size, size, 3), dtype=np.uint8) * 255

    # Calculate the size of the colored boxes
    box_size = size // 10

    # Create black box in the top-left corner
    image[:box_size, :box_size] = (0, 0, 0)

    # Create blue box in the top-right corner
    image[:box_size, -box_size:] = (255, 0, 0)

    # Create green box in the bottom-left corner
    image[-box_size:, :box_size] = (0, 255, 0)

    # Create red box in the bottom-right corner
    image[-box_size:, -box_size:] = (0, 0, 255)

    # Display the image
    cv2.imshow('Colored Boxes Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
# Prompt the user to enter the size of the image
size = int(input("Enter the size of the image: "))

# Create the colored boxes image
create_colored_boxes(size)
