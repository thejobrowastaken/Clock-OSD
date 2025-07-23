from customtkinter import *
from time import strftime

#Variables
MainMenuTxt = "ClockV2"
MenuWidgetRounding = 40


#MainRootSETUPS
root = CTk()
root.geometry("400x400")

#Grid Creation
root.columnconfigure((0,1,2,3,4), weight=2)
root.rowconfigure((0,1,2,3,4), weight=2)

#Def Function Storage
def clock():
    global TimeLabel
    DigitalClock = CTkToplevel()
    DigitalClock.columnconfigure(1, weight=2)
    DigitalClock.rowconfigure(1, weight=2)
    DigitalClock.geometry()
    DigitalClock.attributes("-topmost", 1)
    TimeLabel = CTkLabel(DigitalClock, text="test", font=("Arial", 56, "bold"))
    TimeLabel.grid(row=1, column=1, sticky="news")
    def Tick():
        global TimeLabel
        Currenttime = strftime("%H:%M:%S")
        TimeLabel.configure(text=Currenttime)
        TimeLabel.after(1000, Tick)
    Tick()



#Settings
MainMenuText = CTkLabel(master=root, text=MainMenuTxt, font=("Arial", 20, "bold"))
Clockbtn = CTkButton(master=root, text="test", corner_radius=MenuWidgetRounding, command=clock)
SettingsBtn = CTkButton(master=root, text="Settings", corner_radius=MenuWidgetRounding)
Quitbtn = CTkButton(master=root, text="Quit", corner_radius=MenuWidgetRounding)

#MainMenuGridding
MainMenuText.grid(row=0, column=2, sticky="new", pady=10)
Clockbtn.grid(row=1, column=2, sticky="NEWS",pady=10)
SettingsBtn.grid(row=2, column=2, sticky="News",pady=10)
Quitbtn.grid(row=3, column=2, sticky="news",pady=10)

root.mainloop() #Mainloop.
