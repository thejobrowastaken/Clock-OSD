from tkinter import *
from tkinter import colorchooser
from time import strftime, sleep
#Globals
global scaleheight

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
colourpickervalue = '#8db3f0'
global scaleheight
def ColourSelecter():
    global colourpickervalue
    colourpickervalue = colorchooser.askcolor()
    colourpickervalue = colourpickervalue[1] #Always put [1] as it signifys the colour to be in hexadecimal form!!

def Settings():  #I dont know what im doing but i know itll work barely
    global scaleheight       
    Title.config(text="Setup")
    Clock.config(text="Colour Picker", command=ColourSelecter)
    fontscale = Scale(Root,from_=1, to=30, orient="horizontal", bg=bgColour, fg=fgColour)
    fontscale.set(15)
    scaleheight = fontscale.get()
    fontlabel = Label(Root, text="fontscale", bg=bgColour, font=("Arial", 10, "bold"), fg=fgColour)
    fontlabel.grid(row=2, column=1, sticky="wn")
    fontscale.grid(row=2, column=1, sticky="w")
    Customize.destroy()


    
def DigitalClock(): 
    global scaleheight
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
        global scaleheight
        a = strftime('%H:%M:%S')
        lb.config(text=a, fg=colourpickervalue, font=("Arial", scaleheight, "bold"))
        lb.after(1000,clocktime)
    lb = Label(root, width=25, height=1, bg='black', fg='#8db3f0', font=("Arial", 35, 'bold'))
    lb.pack()
    clocktime()
    root.mainloop()
    





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
