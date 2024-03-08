import cv2

def resize_image(image_path, scale_factor):
    # Read the image
    image = cv2.imread(image_path)

    # Resize the image to a larger size
    larger_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)

    # Resize the image to a smaller size
    smaller_image = cv2.resize(image, None, fx=1/scale_factor, fy=1/scale_factor, interpolation=cv2.INTER_LINEAR)

    # Display the original, larger, and smaller images
    cv2.imshow('Original Image', image)
    cv2.imshow('Larger Image', larger_image)
    cv2.imshow('Smaller Image', smaller_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage:
# Resize the image to 2 times larger and 2 times smaller
resize_image('C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg', scale_factor=2)
