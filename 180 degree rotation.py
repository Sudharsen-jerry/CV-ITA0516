import cv2
path = 'C:\\Users\\ADMIN\\Desktop\\Computer vision\\doctor.jpg'
src = cv2.imread(path)
rotated_image = cv2.rotate(src, cv2.ROTATE_180)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
