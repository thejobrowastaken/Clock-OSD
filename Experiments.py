#code to experiment with

from tkinter import *

root = Tk()
root.config(bg="grey")
root.geometry('800x800')
root.title("grid test")

def float():
    lb1.config(text="0.1123")

def int():
    lb1.config(text=2020)

def string():
    lb1.config(text="Taiwan is a country")

def textpick():
    a = Txt.get("1.0",'end-1c')
    a = str(a)
    lb1.config(text=a)

root.rowconfigure((0,1,2,3,4,5,6,7,8), weight=2)
root.columnconfigure((0,1,2,3,4,5,6,7,8), weight=2)

lb1 = Label(text="Hello World", font=("Arial", 10, 'bold'), bg="blue", fg="#8db8f0")
bt1 = Button(text="float", font=("Arial", 10, 'bold'), bg="Black", fg="#8db8f0", command=float)
bt2 = Button(text="Int", font=("Arial", 10, 'bold'), bg="Black", fg="#8db8f0", command=int)
bt3 = Button(text="String", font=("Arial", 10, 'bold'), bg="Black", fg="#8db8f0", command=string)
Txt = Text(root, bg="black", fg="#00ff44", font=("Arial", 10, "italic"))
txtbtn = Button(root, bg="Yellow", fg="#8db8f0",font=("Arial", 10, 'bold'), command=textpick)

lb1.grid(row=0, column=4,  sticky="nsew", padx=20, pady=20)
bt1.grid(row=4, column=0,  sticky="nswe", columnspan=2, padx=20, pady=20)
bt2.grid(row=5, column=0,  sticky="nswe", columnspan=2, padx=20, pady=20)
bt3.grid(row=6, column=0,  sticky="nswe", columnspan=2, padx=20, pady=20)
Txt.grid(row=3, column=4, sticky="ew")
txtbtn.grid(row=4, column=4, sticky="ew")
root.mainloop()
