from tkinter import *
from Sketchpad import Sketchpad


root = Tk()
root.geometry("1000x1000")
root.update_idletasks()

sketchpad = Sketchpad(root, 500, 500)
sketchpad.pack(expand=True, fill='both')

root.mainloop()


