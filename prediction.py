import cv2
import numpy as np
 
#engine = pyttsx3.init()
list1=[1,2,3,4,5,6,7,8,9,10]
list2=['pulkit ','ranjan','nishant','unknown','unknown']
font = cv2.FONT_HERSHEY_SIMPLEX
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
recognizer = cv2.createLBPHFaceRecognizer()#algorith for learning on the face
recognizer.load('trainner/trainner.yml')#path where the result of training set is done
Id=0#for the ids from the photo
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 2, 1, 1, 1, 2)#for the font of the text
while True:
    ret,img=cam.read()#read the image
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#converting into gray scale image
    faces=faceDetect.detectMultiScale(gray, 1.3,5)#for detcting the multiple faces
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,128,0),2)# for the face size Ie length till where the face need to be scanned length and be=readth
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])# fro getting the ids for  the face
        if Id in list1:
            Id=list2[Id-1]
        cv2.cv.PutText(cv2.cv.fromarray(img),str(Id), (x,y+h),font,(0,0,255))# for desplaying the result below the image
        #engine.say("Pulkit")
    cv2.imshow('images',img) 
    if(cv2.waitKey(1)==ord('q')):#once done for quitiong press q
        break
#engine.runAndWait()
cam.release()
cv2.destroyAllWindows()
