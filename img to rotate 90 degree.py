import cv2

def rotate_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Rotate the image 90 degrees clockwise along the y-axis
    rotated_image = cv2.flip(image, 1)

    # Display the original and rotated images
    cv2.imshow('Original Image', image)
    cv2.imshow('Rotated Image', rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
# Rotate the image 90 degrees clockwise along the y-axis
rotate_image('C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg')
