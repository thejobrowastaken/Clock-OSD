from tkinter import *
from tkinter import colorchooser, font
from tkinter.ttk import Combobox
from time import strftime, sleep

#Items requiring outside of mainloop
def kill():
    quit()

#Variables 
bgColour='#b0c3e8'
DrkBgColour = '#b1c2e3'
fgColour = '#020c21'
Font_Of_Title = ("Arial", 20, "bold")
Common_Font = ("Arial", 15, "bold")
scaleheight = 35
colourpickervalue = '#8db3f0'
clocklabelwidth = 25
TimeType = "%H:%M:%S"
SelectedRadioButton = 24




#The Great List Of Fonts
Root = Tk()

#Variables Requiring a dependant Root
SelectedFontValue = StringVar(Root) #Stores the combobox of fonts value in a string variable!



Root.geometry('400x400')
Root.title("Clock V2")
Root.config(bg=bgColour)
#Root Info

#Func storage
def ColourSelecter():
    global colourpickervalue
    colourpickervalue = colorchooser.askcolor()
    colourpickervalue = colourpickervalue[1] #Always put [1] as it signifys the colour to be in hexadecimal form!!

#RadioButtons Functions. pls dont touch if it works
def pilottime():
            global TimeType
            TimeType = "%H:%M:%S"
def commontime():
            global TimeType
            TimeType = "%I:%M:%S %p"


def Settings():
    global scaleheight, fontscale, fontlabel, back_button, colour_picker_btn, Pilotttime, Commontime, FontList
    
    # Hide original buttons
    Clock.grid_remove()
    Customize.grid_remove()
    quitbtn.grid_remove()
    
    Title.config(text="Setup")
    
    # Create Back button
    back_button = Button(Root, text="Back", bg=bgColour, font=Common_Font, fg=fgColour, command=RestoreMainMenu)
    back_button.grid(row=3, column=1, columnspan=2, sticky='wne')
    
    # Colour Picker Button
    colour_picker_btn = Button(Root, text="Colour Picker", bg=bgColour, font=Common_Font, fg=fgColour, command=ColourSelecter)
    colour_picker_btn.grid(row=1, column=1, columnspan=2, sticky='wne')
    
    # Font Scale Slider
    fontlabel = Label(Root, text="Font Scale", bg=bgColour, font=("Arial", 10, "bold"), fg=fgColour)
    fontlabel.grid(row=2, column=1, sticky="wn")
    
    fontscale = Scale(Root, from_=1, to=150, orient="horizontal", bg=bgColour, fg=fgColour)
    fontscale.set(scaleheight)
    fontscale.grid(row=2, column=1, sticky="w")
    
    def updatescale(val):
        global scaleheight
        scaleheight = int(float(val))
    
    fontscale.config(command=updatescale)

    #Radiobuttons for 12h and 24h
    Pilotttime = Radiobutton(Root, text="24Hour format", value=24,variable=SelectedRadioButton, bg=bgColour, command=pilottime)
    Commontime = Radiobutton(Root, text="12Hour format", value=12,variable=SelectedRadioButton, bg=bgColour, command=commontime)
    Pilotttime.grid(row=2, column=2, sticky="news",pady=10)
    Commontime.grid(row=2, column=2, sticky="sew", pady=10)


    
    #Listbox Creation
    ListOfFonts = font.families()
    FontList = Combobox(Root, values=ListOfFonts, background=DrkBgColour)
    FontList.grid(row=1, column=2, sticky="s")


def RestoreMainMenu():
    # Remove settings widgets
    fontscale.grid_remove()
    fontlabel.grid_remove()
    back_button.grid_remove()
    colour_picker_btn.grid_remove()
    Pilotttime.grid_remove()
    Commontime.grid_remove()
    FontList.grid_remove()

    
    # Restore original buttons
    Title.config(text="ClockMenu")
    Clock.grid()
    Customize.grid()
    quitbtn.grid()

def Digitalclock():
    global Clockroot
    Clockroot = Toplevel()  # Changed from Tk() to Toplevel()

    #Getting widths and heights
    x_screenreso = Clockroot.winfo_screenmmwidth()  # Changed from root to Root
    y_screenreso = Clockroot.winfo_screenmmheight()  # Changed from root to Root
    window_x = Clockroot.winfo_width()
    window_y = Clockroot.winfo_height()
    errorx = 60
    errory = 30
    print(window_x, window_y)


    Clockroot.resizable(False,False)
    Clockroot.config(bg='black') 

    #Position Calculation
    xresoclock = (int(x_screenreso / 2)) + int(window_x / 2 )
    yresoclock = (int(y_screenreso / 2)) + int(window_y / 2 )


    #Position Placement
    Clockroot.geometry(f"+{int(xresoclock)}+{int(yresoclock)}")
    Clockroot.attributes('-topmost', True)
    Clockroot.wm_attributes('-transparent', 'black')
    Clockroot.wm_overrideredirect(1)

    #Time Getter Function
    def clocktime():
        a = strftime(TimeType)
        lb.config(text=a, fg=colourpickervalue, font=(f'{FontList.get()}', int(scaleheight), "bold"))
        lb.after(1000,clocktime)

    #God knows what All of this is
    global lb
    lb = Label(Clockroot, width=clocklabelwidth, height=1, bg='black', fg='#8db3f0', font=("Arial", 35, 'bold'))
    lb.pack()
    clocktime()
    Clock.config(command=ClockKiller) #Sets the command to the other function
    Clockroot.update()


#This will toggle the clock off
def ClockKiller():
    Clockroot.destroy()
    Clock.config(command=Digitalclock) #Vice Versa the command
    




Root.rowconfigure((0,1,2,3), weight=2)
Root.columnconfigure((0,1,2,3), weight=2)
#Rows and Columns

#Titles
Title = Label(Root, text="ClockMenu", bg=bgColour, font=("Arial", 20, "bold"), fg=fgColour)
Clock = Button(Root, text="Clock", bg=bgColour, font=Common_Font, fg=fgColour, command=Digitalclock)
Customize = Button(Root, text="Customization", bg=bgColour, font=Common_Font, fg=fgColour, command=Settings)
quitbtn = Button(Root, text="Quit", bg=bgColour, font=Common_Font, fg=fgColour, command=kill)

Title.grid(row=0, column=1, columnspan=2, sticky="wne", pady=20)
Clock.grid(row=1, column=1, columnspan=2, sticky='wne')
Customize.grid(row=2, column=1, columnspan=2, sticky='wne')
quitbtn.grid(row=3, column=1, columnspan=2, sticky='wne')

Root.mainloop()
