import cv2 as cv
smile_cascade=cv.CascadeClassifier("C:\\Users\\ADMIN\\Desktop\\Computer vision\\haarcascade_smile.xml")
path= 'C:\\Users\\ADMIN\\Desktop\\Computer vision\\two.jpg'
img=cv.imread(path)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
smile=smile_cascade.detectMultiScale(gray,1.9,11)
for (x,y,w,h) in smile:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv.imwrite("Output22_Smile_dection.jpg",img)
