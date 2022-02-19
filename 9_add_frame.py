from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Add frame")

frame = LabelFrame(root,text="This is my frame..",padx=5,pady=5)
frame.pack(padx=10,pady=10) # frame x=10 & y =10 to the left and right windows

b = Button(frame,text="Click button")
b.grid(row=0,column=0)





root.mainloop()
     
