import tkinter
import cv2
import tkinter.messagebox as msgbox
import DBConnect.dbManage
from tkinter import *
from gaze_tracking import GazeTracking
# import numpy as np


db_controller=DBConnect.dbManage.MysqlController('127.0.0.1','root', 'dPdms7942','concentration', 3300)
studentNumber=201811218
studentName='김효진'
totalPoint=70
minusPoint=0
db_controller.insert_user(studentNumber,studentName)
gaze=GazeTracking()
webcam=cv2.VideoCapture(0)
cnt=0

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



# import tkinter
# import cv2
# import numpy as np
# import time
# from tkinter import *
# from tkinter import messagebox
# import pandas as pd
# import ctypes
# import random

# def closebox():
#     window.destroy()
#     facing = True

# def closeRbox():
#     Rwindow.destroy()
#     RFlag = True

# # xml 경로 바꿨음
# xml='C:/python_opencv/haarcascades/haarcascade_frontalface_default.xml'
# bodyxml='C:/python_opencv/haarcascades/haarcascade_upperbody.xml'
# face_cascade=cv2.CascadeClassifier(xml)
# body_cascade=cv2.CascadeClassifier(bodyxml)

# cap=cv2.VideoCapture(0)
# cap.set(3,640)
# cap.set(4,480)
# def createWindow():
#     window = Tk()
#     window.title("경고")
#     window.geometry("400x100-320+240")
#     label = tkinter.Label(window, text = "\n자리벗어남 감지\n자리로 돌아와\n확인을 눌러주세요")
#     label.pack()
#     btn1 = Button(window, text = "확인", command=closebox)
#     btn1.pack(side='bottom')

#     return window;

# def createRandomWindow():
#     Rwindow = Tk()
#     Rwindow.title("경고")
#     Rwindow.geometry("400x100-320+240")
#     label = tkinter.Label(Rwindow, text = "\n집중도 확인메시지입니다.\n확인을 눌러주세요")
#     label.pack()
#     btn1 = Button(Rwindow, text = "확인", command=closeRbox)
#     btn1.pack(side='bottom')

#     return Rwindow;

# count = 0
# checkTime = time.time()
# now = time.time()
# facing = True
# RFlag = True #랜덤플래그
# window = createWindow()
# Rwindow = createRandomWindow()
# concentrate = 50
# checkRandomTime = time.time()
# Rnum = 0

# while(True):
#     # print(facing);
#     now = time.time()
#     ret,frame=cap.read()
#     frame=cv2.flip(frame,1)
#     gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#     if(RFlag == True):
#         checkRandomTime = time.time()
#         Rnum = random.randrange(2, 5)
#         RFlag=False

#     faces=face_cascade.detectMultiScale(gray,1.05,5)
#     body=body_cascade.detectMultiScale(gray,1.05,5)

#     #print("Number of faces detected: "+str(len(faces)))

#     if len(faces):
#         facing = True
#         checkTime = time.time()
#         for(x,y,w,h) in faces:
#             cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
#     if len(body):
#         for(x,y,w,h) in body:
#             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)


#     cv2.imshow('result',frame)

#     #얼굴이 인식 안되는 상태고 facing이 true일때로 조건을 둬서 checktime이 한번만 갱신되게끔
#     if(len(faces) == 0 and facing):
#         facing = False
#         checkTime = time.time()
    
#     if((now-checkTime) > 5 and not facing):
#         # loop.run_until_complete(ATest())
#         # loop.close
#         count += 1
#         window.mainloop()
#         window = createWindow()

#     if((now-checkRandomTime) > Rnum and (concentrate < 60) and not RFlag):
#         checkRandomTime = time.time()
#         Rwindow.mainloop()
#         Rwindow = createRandomWindow()


#     k=cv2.waitKey(30)&0xff
#     if k==27:
#         raw_data = {'얼굴인식 안된 횟수' : [count]}
#         raw_data = pd.DataFrame(raw_data)
#         raw_data.to_excel(excel_writer='sample1.xlsx')
#         break

# cap.release()
# cv2.destroyAllWindows()    
