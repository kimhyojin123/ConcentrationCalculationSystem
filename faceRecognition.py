import tkinter
import cv2
import tkinter.messagebox as msgbox
import DBConnect.dbManage
from tkinter import *
from gaze_tracking import GazeTracking
# import numpy as np

# xml='C:/Users/XNOTE/Downloads/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml'
# face_cascade=cv2.CascadeClassifier(xml)
db_controller=DBConnect.dbManage.MysqlController('127.0.0.1','root', 'dPdms7942','concentration', 3300)
studentNumber=201811218
studentName='김효진'
totalPoint=70
minusPoint=0
db_controller.insert_user(studentNumber,studentName)
gaze=GazeTracking()
webcam=cv2.VideoCapture(0)
cnt=0
# cap.set(3,640)
# cap.set(4,480)

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()
    frame=cv2.flip(frame,1)
    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    if(left_pupil==None and right_pupil==None):
        if cnt==30:
            minusPoint+=1;
            db_controller.update_outOfPosition(studentNumber,minusPoint,totalPoint-(5*minusPoint))
            msgbox.showwarning("경고","얼굴인식이 되지 않습니다.\n")
            cnt=0
        else :
            cnt+=1;    
        
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break


# cap.release()
# cv2.destroyAllWindows() 


# ret,frame=cap.read()
    # frame=cv2.flip(frame,1)
    # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    # faces=face_cascade.detectMultiScale(gray,1.05,5)
    # print("Number of faces detected: "+str(len(faces)))

    # if len(faces):
    #     for(x,y,w,h) in faces:
    #         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    # cv2.imshow('result',frame)
    
    # k=cv2.waitKey(30)&0xff
    # if k==27:
    #     break 



    # ret,frame=cap.read()
    # if ret is False:
    #     break
    # frame=cv2.flip(frame,1)
    # roi=frame[0:4480,0:3640]
    # rows,cols,_=roi.shape

    # gray_roi=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    # gray_roi=cv2.GaussianBlur(gray_roi,(7,7),0)

    # _, threshold=cv2.threshold(gray_roi,3,255,cv2.THRESH_BINARY_INV)
    # contours, _=cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    # contours=sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)

    # for cnt in contours:
    #     (x,y,w,h)=cv2.boundingRect(cnt)
    #     cv2.rectangle(roi,(x,y),(x+w,y+h),(255,0,0),2)
    #     cv2.line(roi,(x+int(w/2),0),(x+int(w/2),rows),(0,255,0),2)
    #     cv2.line(roi,(0,y+int(h/2)),(cols,y+int(h/2)),(0,255,0),2)
    #     break

