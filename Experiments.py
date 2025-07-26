from customtkinter import *
from tkinter import *
from PIL import Image, ImageTk

#I want those 20 bucks ishika im doing all this for you

#Basic Variables
Bg = "#25294F"
DarkerBg = "#1b1e3b"
Fg = "#D11F77"
ButtonColour = "#F7608B"
root = CTk()
root.config(bg="#25294F")
CodeAssets = "C:\\Users\\Sharad Keny\\Pictures\\Code Assets\\menuColour.png"
ParagraphA = ""

#Photo image conversion
OriginalImage = Image.open(CodeAssets)
ResizedImg = OriginalImage.resize((70,60), Image.LANCZOS)
tkimage = ImageTk.PhotoImage(ResizedImg)

#Root dependent variables
ScreenX = root.winfo_screenwidth()
ScreenY = root.winfo_screenheight()
ScreenX = ScreenX
#Sizing
root.geometry("{}x{}+-8+-4".format(ScreenX, ScreenY))

#Gridding
root.columnconfigure((0,1,2,3,4,5,6,7,8), weight=1)
root.rowconfigure((0,1,2,3,4,5,6,7,8), weight=1)

#Func Storage
def SideMenu():
    global Sidebar, PwNotes, PwLectures
    Sidebar.grid(row=0, column=0, rowspan=9, sticky="news")
    PwBatches.grid(row=1, column=0, sticky="nsew", padx=40, pady=40)
    PwNotes.grid(row=2, column=0, sticky="nsew", padx=40, pady=40)
    PwLectures.grid(row=3, column=0, sticky="nsew", padx=40, pady=40)
    PwLinks.grid(row=4, column=0, sticky="nsew", padx=40, pady=40)
    SideMenuThingy.grid(row=1, column=0, sticky="nsew", padx=40, pady=40)

#Elements
Titlefont = CTkFont(weight="bold", slant="italic", size=65, family="Lexend")
ParaFont = CTkFont(size=1, family="Lexend")
TitlePhysic = CTkLabel(root, text="PHYSICS", font=Titlefont, bg_color=Bg, text_color=Fg, width=20, padx=-100)
TitleWallah = CTkLabel(root, text="WALLAH", font=Titlefont, bg_color=Bg, text_color=Fg, width=20,padx=100)
Paragraphone = CTkLabel(root, text=ParagraphA, font=Titlefont)
SideBarBtn = CTkButton(root,image=tkimage, fg_color=Bg, font=("Lexend", 10, "bold"), height=1, width=1, text="", command=SideMenu)
Sidebar = CTkLabel(root, text="", bg_color=DarkerBg, corner_radius=30)
PwBatches = CTkButton(root, text="Batches", fg_color=ButtonColour)
PwNotes = CTkButton(root, text="Batches", fg_color=ButtonColour)
PwLectures = CTkButton(root, text="Lectures", fg_color=ButtonColour)
PwLinks = CTkButton(root, text="GroupLinks", fg_color=ButtonColour)
SideMenuThingy = CTkLabel(root, text="Options", font=Titlefont, bg_color="#FD6DEE", text_color='#FD6DEE')


#GriddingElementos
TitlePhysic.grid(row=0, column=4, sticky = "ws")
TitleWallah.grid(row=1, column=4, sticky="ne")
SideBarBtn.grid(row=0, column=0, sticky="nw", pady=20, padx=20)
Paragraphone.grid(row=3, column=4)


root.mainloop()
