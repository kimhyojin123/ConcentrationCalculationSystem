import tkinter
from tkinter import *
from tkinter import messagebox

def closebox():
    window.destroy()
    window.quit();

def createWindow():
    window = Tk()
    window.title("경고")
    window.geometry("400x100-320+240")
    label = tkinter.Label(window, text = "\n자리벗어남 감지\n자리로 돌아와\n확인을 눌러주세요")
    label.pack()
    btn1 = Button(window, text = "확인", command=closebox)
    btn1.pack(side='bottom')

    return window;


window = createWindow()

btn1 = Button(window, text = "확인", command=closebox)
btn1.pack(side='bottom')

window.mainloop()