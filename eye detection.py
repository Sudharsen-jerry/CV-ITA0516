import cv2 as cv
eye_cascade=cv.CascadeClassifier('C:\\Users\\ADMIN\\Desktop\\Computer vision\\haarcascade_eye.xml')
img=cv.imread('C:\\Users\\ADMIN\\Desktop\\Computer vision\\two.jpg')
eye=eye_cascade.detectMultiScale(img,1.9,2)
for (x,y,w,h) in eye:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv.imwrite("Output21_Eye_Detection.jpg",img)
