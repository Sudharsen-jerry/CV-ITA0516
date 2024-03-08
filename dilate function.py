import cv2
image_path = 'C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg'
image = cv2.imread(image_path)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) 
dilated_image = cv2.dilate(image, kernel, iterations=1)  
cv2.imshow('Original Image', image)
cv2.imshow('Dilated Image', dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
