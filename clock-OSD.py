from tkinter import *
from time import strftime

menu = Tk()
menu.geometry("200x400")
Lb = Label(menu,
        text="Menu",
        font=("Arial", 20),
        width=40, height=1, bg="#C76767")
Lb.pack()



menu.mainloop()




def DigitalClock():
    root = Tk()
    root.resizable(False,False)
    root.config(bg='black')
    root.geometry('320x100+500+500')
    root.attributes('-topmost', True)
    root.wm_attributes('-transparent', 'black')
    root.wm_overrideredirect(1)
    def clocktime():
        a = strftime('%H:%M:%S')
        lb.config(text=a)
        lb.after(1000,clocktime)
    lb = Label(root, width=25, height=1, bg='black', fg="cyan", font=("Arial", 60, 'bold'))
    lb.pack()
    clocktime()
    root.mainloop()





