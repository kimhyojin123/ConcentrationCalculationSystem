import cv2
import tkinter.messagebox as msgbox
import DBConnect.dbManage
from tkinter import *
from gaze_tracking import GazeTracking
import tkinter
import numpy as np
import time
from tkinter import messagebox
import pandas as pd
import ctypes
import random
from threading import Thread

def closebox():
    window.destroy()
    facing = True

def closeRbox():
    Rwindow.destroy()
    RFlag = True

def closePupilbox():
    Pupilwindow.destroy()
    PupilFlag = False

xml='C:/Users/XNOTE/Downloads/opencv/sources/data/haarcascades/haarcascade_frontalface_default.xml'
bodyxml='C:/Users/XNOTE/Downloads/opencv/sources/data/haarcascades/haarcascade_upperbody.xml'
smile_detector = cv2.CascadeClassifier('C:/Users/XNOTE/Downloads/opencv/sources/data/haarcascades/haarcascade_smile.xml')
face_cascade=cv2.CascadeClassifier(xml)
body_cascade=cv2.CascadeClassifier(bodyxml)
db_controller=DBConnect.dbManage.MysqlController('127.0.0.1','root', 'dPdms7942','concentration', 3300)
studentNumber=201811218
studentName='김효진'
totalPoint=70
sightPoint=0
db_controller.insert_user(studentNumber,studentName)
gaze=GazeTracking()
webcam=cv2.VideoCapture(0)
cnt=0

webcam.set(3,640)
webcam.set(4,480)
# 알림창 같이 뜨는거 해결해야함
def createWindow():
    window = Tk()
    window.title("경고")
    window.geometry("400x100-320+240")
    label = tkinter.Label(window, text = "\n자리벗어남 감지\n자리로 돌아와\n확인을 눌러주세요")
    label.pack()
    btn1 = Button(window, text = "확인", command=closebox)
    btn1.pack(side='bottom')

    return window;


def createRandomWindow():
    Rwindow = Tk()
    Rwindow.title("경고")
    Rwindow.geometry("400x100-320+240")
    label = tkinter.Label(Rwindow, text = "\n집중도 확인메시지입니다.\n확인을 눌러주세요")
    label.pack()
    btn1 = Button(Rwindow, text = "확인", command=closeRbox)
    btn1.pack(side='bottom')

    return Rwindow;

def createPupilWindow():
    Pupilwindow = Tk()
    Pupilwindow.title("경고")
    Pupilwindow.geometry("400x100-320+240")
    label = tkinter.Label(Pupilwindow, text = "\n시선이 제대로 인식되지 않습니다.\n확인을 누르고 카메라에 얼굴을 제대로 보여주세요.")
    label.pack()
    btn1 = Button(Pupilwindow, text = "확인", command=closePupilbox)
    btn1.pack(side='bottom')

    return Pupilwindow;

positionPoint = 0 
smilePoint=0
checkTime = time.time()
now = time.time()
facing = True
RFlag = True #랜덤플래그
PupilFlag = False
window = createWindow()
Rwindow = createRandomWindow()
Pupilwindow = createPupilWindow()
checkRandomTime = time.time()
checkSmileTime = time.time()
Rnum = 0


# t1 = Thread(target = window.mainloop())
# t2 = Thread(target = Rwindow.mainloop())

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    if(RFlag == True):
        checkRandomTime = time.time()
        Rnum = random.randrange(2, 5)
        RFlag=False

    faces=face_cascade.detectMultiScale(gray,1.05,5)
    body=body_cascade.detectMultiScale(gray,1.05,5)
    smile = smile_detector.detectMultiScale(gray, 1.8,20)
        # Label the face as smiling 

    now = time.time()

    if len(faces):
        facing = True
        checkTime = time.time()
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        if len(smile) > 0:
            cv2.putText(frame, 'Smiling', (x,y+h+40), fontScale=3,
            fontFace=cv2.FONT_HERSHEY_PLAIN, color=(255,255,255))
            if((now-checkSmileTime) >30):
                checkSmileTime = time.time()
                smilePoint += 1
            db_controller.update_laughDetection(studentNumber,smilePoint,totalPoint-(5*smilePoint))
    
    if len(body):
        for(x,y,w,h) in body:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
    if(len(faces) == 0 and facing):
        facing = False
        checkTime = time.time()
    
    if((now-checkTime) > 5 and not facing):
        positionPoint += 1
        db_controller.update_outOfPosition(studentNumber,positionPoint,totalPoint-(10*positionPoint))
        # t1.start()
        window.mainloop()
        window = createWindow()

    if((now-checkRandomTime) > Rnum and (totalPoint < 60) and not RFlag):
        checkRandomTime = time.time()
        # t2.start()
        Rwindow.mainloop()
        Rwindow = createRandomWindow()

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
    if(left_pupil==None and right_pupil==None and not PupilFlag):
        if cnt==10:
            PupilFlag = True
            sightPoint+=1;
            db_controller.update_outOfSight(studentNumber,sightPoint,totalPoint-(5*sightPoint))
            Pupilwindow.mainloop()
            Pupilwindow = createPupilWindow()
            cnt=0
        else :
            cnt+=1;    
        
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        db_controller.select_all_to_excel()
        break

webcam.release()
cv2.destroyAllWindows() 