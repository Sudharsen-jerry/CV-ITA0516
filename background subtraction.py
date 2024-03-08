import cv2
bg_subtractor = cv2.createBackgroundSubtractorMOG2()
image_path = 'C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg'
frame = cv2.imread(image_path)
fg_mask = bg_subtractor.apply(frame)
cv2.imshow('Original Image', frame)
cv2.imshow('Foreground Mask', fg_mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
