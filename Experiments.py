from tkinter import *
from tkinter import colorchooser
import tkinter
from time import strftime, sleep

#Items requiring outside of mainloop
def kill():
    quit()

#Variables 
bgColour='#b0c3e8'
fgColour = '#020c21'
Font_Of_Title = ("Arial", 20, "bold")
Common_Font = ("Arial", 15, "bold")
scaleheight = 35
colourpickervalue = '#8db3f0'
clocklabelwidth = 25


Root = Tk()
Root.geometry('400x400')
Root.title("Clock V2")
Root.config(bg=bgColour)
#Root Info

#Func storage
def ColourSelecter():
    global colourpickervalue
    colourpickervalue = colorchooser.askcolor()
    colourpickervalue = colourpickervalue[1] #Always put [1] as it signifys the colour to be in hexadecimal form!!

def Settings():  #I dont know what im doing but i know itll work barely
    global scaleheight       
    Title.config(text="Setup")
    Clock.config(text="Colour Picker", command=ColourSelecter)
    fontscale = Scale(Root,from_=1, to=150, orient="horizontal", bg=bgColour, fg=fgColour)
    fontscale.set(scaleheight)
    scaleheight = fontscale.get()
    fontlabel = Label(Root, text="fontscale", bg=bgColour, font=("Arial", 10, "bold"), fg=fgColour)
    fontlabel.grid(row=2, column=1, sticky="wn")
    def updatescale(val):
        global clocklabelwidth
        global scaleheight
        scaleheight = int(float(val))
        clocklabelwidth = scaleheight + clocklabelwidth
    fontscale.config(command=updatescale)
    fontscale.grid(row=2, column=1, sticky="w")
    Customize.destroy()


    
def DigitalClock(): 
    root = Toplevel()  # Changed from Tk() to Toplevel()
    x_screenreso = root.winfo_screenmmwidth()  # Changed from root to Root
    y_screenreso = root.winfo_screenmmheight()  # Changed from root to Root
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
        lb.config(text=a, fg=colourpickervalue, font=("Arial", int(scaleheight), "bold"))
        lb.after(1000,clocktime)
    global lb
    lb = Label(root, width=clocklabelwidth, height=1, bg='black', fg='#8db3f0', font=("Arial", 35, 'bold'))
    lb.pack()
    clocktime()





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
