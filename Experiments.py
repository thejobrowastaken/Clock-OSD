from tkinter import *

root = Tk()
root.config(bg="grey")
root.geometry("300x700")
lb = Label(root, text="test", font=("Arial", 20, "italic"), width=20, height=3, bg="#CB11F0", fg="black")
lb.grid()
btn = Button(root, text="yes", font=("Arial", 15, "bold"))
root.mainloop()

