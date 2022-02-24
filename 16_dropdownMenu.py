from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


#first windows
root = Tk()
root.title("first window")
root.geometry("400x400")#default windows size


def show():
    myLabel=Label(root,text=clicked.get()).pack()



options=["Mon","Tue","Wed","Thur","Fri"]
#dropdown box
clicked=StringVar()
clicked.set(options[0])

drop=OptionMenu(root,clicked,*options)
drop.pack()

myButton=Button(root,text="click",command=show).pack()

root.mainloop()
     
