import cv2
face_cascade = cv2.CascadeClassifier('C:\\Users\\ADMIN\\Desktop\\Computer vision\\cars.xml')
vc = cv2.VideoCapture('C:\\Users\\ADMIN\\Desktop\\Computer vision\\videoplayback.mp4')
if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False

while rval:
    rval, frame = vc.read()
    cars = face_cascade.detectMultiScale(frame, 9.1, 2)
    ncars = 0
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        ncars = ncars + 1
        cv2.imwrite("Result.jpg",frame)
