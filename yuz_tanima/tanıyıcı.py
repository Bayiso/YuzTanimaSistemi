import cv2
import numpy as np
import os
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
faceCascade = cv2.CascadeClassifier("Cascade/haarcascade_frontalface_default.xml")
font = cv2.FONT_HERSHEY_SIMPLEX
id = 4
names = ['None', 'benavo',"şerino", "nıza"]

cam = cv2.VideoCapture(1)
#cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#cam.set(3, 640)
#cam.set(4, 480)

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
while True:
    ret, img =cam.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(int(minW), int(minH)),)
    for (x, y, w, h) in faces:

        """color = img[y:y + h, x:x + w]"""
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        if (confidence < 100):
            id = names[2]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "bilinmiyor"
            confidence = "  {0}%".format(round(100 - confidence))
        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        """img_item = "my_image.jpg"
        cv2.imwrite(img_item,color)"""

    cv2.imshow('camera', img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
cam.release()
cv2.destroyAllWindows()
