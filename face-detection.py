import cv2

#here enter your path to haarcascade_frontalface_default
face_cascade = cv2.CascadeClassifier('C://Users//JASWANTH//PycharmProjects//telebot//venv//Lib//site-packages//cv2//data//haarcascade_frontalface_default.xml')

#reading the image
img = cv2.imread('test.jpg')  

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('MY WINDOW',img)

cv2.waitKey(0)