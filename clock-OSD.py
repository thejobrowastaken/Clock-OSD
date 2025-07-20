from tkinter import *
from tkinter import colorchooser
from time import strftime

def settings():
    settings = Tk()
    settings.geometry('300x300')
    settings.title('settings')

    settings.columnconfigure((0,1,2,3,4), weight=2)
    settings.rowconfigure((1,2,3,4), weight=2)

    def colourcmd():
        colour = colorchooser.askcolor()
        colour = colour[1]
        global holdmybeer
        holdmybeer = colour
    settings.config(bg="#8db3f0")
    lb = Label(settings, bg="#8db3f0", fg="white", font=("Arial", 25, "bold"), text="Settings")
    colourpick = Button(settings,bg='#8db3f0', fg="white", command=colourcmd, text="Colour")
    lb.grid(row=0, column=2, sticky="w")
    colourpick.grid(row=1, column=0, columnspan=1, sticky="ew", padx=10)
    
    settings.mainloop()

holdmybeer = '#8db3f0'

def killer():
    quit()


def DigitalClock(): 
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
        lb.config(fg=holdmybeer)
        lb.after(1000,clocktime)
    lb = Label(root, width=25, height=1, bg='black', fg=holdmybeer, font=("Arial", 35, 'bold'))
    lb.pack()
    clocktime()
    root.mainloop()




menu = Tk()
menu.config(bg="#8db3f0")
a = "Clock"
menu.title(a)
x_screenreso = menu.winfo_screenmmwidth()
y_screenreso = menu.winfo_screenmmheight()
xreso = x_screenreso/2 + 565
yreso = y_screenreso/2 + 100
menu.geometry(f"200x400+{int(xreso)}+{int(yreso)}")

menu.rowconfigure((0,1,2,3,4), weight=2)
menu.columnconfigure((0,1,2), weight=2)
lb = Label(menu, text="Da Menu", fg="white", bg="#8db3f0", font=("Arial", 25, "bold"))
settingbtn = Button(menu, text="Settings", fg="white", bg="#8db3f0",font=("Arial", 25, "bold"), command=settings)
clockbtn = Button(menu, text="  Clock  ", fg="white", bg="#8db3f0",font=("Arial", 25, "bold"), command=DigitalClock)
quitbtn = Button(menu, text="quit", fg="white", bg="#8db3f0",font=("Arial", 25, "bold"), command=killer)
note = Label(menu, text="Note:only clock works for now", fg="white", bg="#8db3f0",font=("Arial", 10, "italic"))

lb.grid(row=0, column=1, sticky="n", pady=10)
settingbtn.grid(row=1, column=1, sticky="new")
clockbtn.grid(row=2, column=1, sticky="new")
quitbtn.grid(row=3, column=1,sticky="new")
note.grid(row=4, columnspan=3)
menu.mainloop()






