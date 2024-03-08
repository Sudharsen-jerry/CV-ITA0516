import cv2
import matplotlib.pyplot as plt

def analyze_histogram(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to RGB (OpenCV uses BGR by default)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Calculate histogram for each color channel
    hist_r = cv2.calcHist([image_rgb], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([image_rgb], [1], None, [256], [0, 256])
    hist_b = cv2.calcHist([image_rgb], [2], None, [256], [0, 256])

    # Plot histograms
    plt.figure(figsize=(10, 5))
    plt.plot(hist_r, color='red', label='Red')
    plt.plot(hist_g, color='green', label='Green')
    plt.plot(hist_b, color='blue', label='Blue')
    plt.title('Histogram of Color Levels')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid()
    plt.show()

# Example usage
image_path = 'C:\\Users\\ADMIN\\Desktop\\Computer vision\\Histogram-6.png'
analyze_histogram(image_path)
