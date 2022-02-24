from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


#first windows
root = Tk()
root.title("first window")
root.geometry("400x400")#default windows size


def show(): 
    myLabel = Label(root,text=var.get()).pack()

var = IntVar()
c= Checkbutton(root, text="Check box",variable = var)
c.pack()



myButton= Button(root,text="show selection",command=show).pack()




root.mainloop()
     
