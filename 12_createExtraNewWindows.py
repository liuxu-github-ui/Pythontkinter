from tkinter import *
from PIL import ImageTk,Image


#first windows
root = Tk()
root.title("first window")


#second windows
top = Toplevel()
top.title("second window")
my_img= ImageTk.PhotoImage(Image.open("download.png"))
my_label=Label(top,image=my_img).pack()



root.mainloop()
     
