import tkinter
import cv2
import numpy as np
import time
from tkinter import *
from tkinter import messagebox
import pandas as pd
import ctypes
# import asyncio #비동기
import threading


def closebox():
    window.destroy()
    facing = True
    # window.quit()

# xml 경로 바꿨음
xml='C:/python_opencv/haarcascades/haarcascade_frontalface_default.xml'
bodyxml='C:/python_opencv/haarcascades/haarcascade_upperbody.xml'
face_cascade=cv2.CascadeClassifier(xml)
body_cascade=cv2.CascadeClassifier(bodyxml)

cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
def createWindow():
    window = Tk()
    window.title("경고")
    window.geometry("400x100-320+240")
    label = tkinter.Label(window, text = "\n자리벗어남 감지\n자리로 돌아와\n확인을 눌러주세요")
    label.pack()
    btn1 = Button(window, text = "확인", command=closebox)
    btn1.pack(side='bottom')

    return window;

count = 0;
checkTime = time.time()
now = time.time()
facing = True
window = createWindow()
# def Arlet(window):
#     window.mainloop()
#     window.createWindow()

t1 = window.mainloop()


while(True):
    # print(facing);
    now = time.time()
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.05,5)
    body=body_cascade.detectMultiScale(gray,1.05,5)

    #print("Number of faces detected: "+str(len(faces)))

    if len(faces):
        facing = True
        checkTime = time.time()
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    if len(body):
        for(x,y,w,h) in body:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)


    cv2.imshow('result',frame)

    #얼굴이 인식 안되는 상태고 facing이 true일때로 조건을 둬서 checktime이 한번만 갱신되게끔
    if(len(faces) == 0 and facing):
        facing = False
        checkTime = time.time()
    
    if((now-checkTime) > 15 and not facing):
        # loop.run_until_complete(ATest())
        # loop.close
        count += 1
        t1.start()
        # window.mainloop()
        window = createWindow()
        # t1.join()

    k=cv2.waitKey(30)&0xff
    if k==27:
        raw_data = {'얼굴인식 안된 횟수' : [count]}
        raw_data = pd.DataFrame(raw_data)
        raw_data.to_excel(excel_writer='sample1.xlsx')
        break

cap.release()
cv2.destroyAllWindows()    
