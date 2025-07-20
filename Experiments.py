#code to experiment with

from tkinter import *
from tkinter import colorchooser
from time import strftime, sleep

#Items requiring outside of mainloop
def kill():
    quit()

#Variables 
bgColour='#b0c3e8'
fgColour = '#020c21'
Font_Of_Title = ("Arial", 20, "bold")
Common_Font = ("Arial", 15, "bold")


Root = Tk()
Root.geometry('400x400')
Root.title("Clock V2")
Root.config(bg=bgColour)
#Root Info

#Func storage
def DigitalClock(): 
    colorpickervalue = '#8db3f0'
    root = Tk()
    x_screenreso = root.winfo_screenmmwidth()
    y_screenreso = root.winfo_screenmmheight()
    root.resizable(False,False)
    root.config(bg='black')
    xresoclock = x_screenreso/2 + 1360  
    yresoclock = y_screenreso/2 - 150
    root.geometry(f"320x100+{int(xresoclock)}+{int(yresoclock)}")
    root.attributes('-topmost', True)
    root.wm_attributes('-transparent', 'black')
    root.wm_overrideredirect(1)
    def clocktime():
        a = strftime('%H:%M:%S')
        lb.config(text=a)
        lb.config(fg=colorpickervalue)
        lb.after(1000,clocktime)
    lb = Label(root, width=25, height=1, bg='black', fg=colorpickervalue, font=("Arial", 35, 'bold'))
    lb.pack()
    clocktime()
    root.mainloop()

def Settings():         #I dont know what im doing but i know itll work barely
    Title.config(text="Setup")
    Clock.config(text="Colour Picker")
    Customize.destroy()

Root.rowconfigure((0,1,2,3), weight=2)
Root.columnconfigure((0,1,2,3), weight=2)
#Rows and Columns

#Titles
Title = Label(Root, text="ClockMenu", bg=bgColour, font=("Arial", 20, "bold"), fg=fgColour)
Clock = Button(Root, text="Clock", bg=bgColour, font=Common_Font, fg=fgColour, command=DigitalClock)
Customize = Button(Root, text="Customization", bg=bgColour, font=Common_Font, fg=fgColour, command=Settings)
quitbtn = Button(Root, text="Quit", bg=bgColour, font=Common_Font, fg=fgColour, command=kill)

Title.grid(row=0, column=1, columnspan=2, sticky="wne", pady=20)
Clock.grid(row=1, column=1, columnspan=2, sticky='wne')
Customize.grid(row=2, column=1, columnspan=2, sticky='wne')
quitbtn.grid(row=3, column=1, columnspan=2, sticky='wne')
Root.mainloop()
