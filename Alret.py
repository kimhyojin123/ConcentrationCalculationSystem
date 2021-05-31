from tkinter import *
# from tkinter import messagebox

def closebox():
    window.destroy()
    window.quit();

window = Tk()
window.title("경고")
window.geometry("400x100")

btn1 = Button(window, text = "확인", command=closebox)
btn1.pack(side='bottom')

window.mainloop()