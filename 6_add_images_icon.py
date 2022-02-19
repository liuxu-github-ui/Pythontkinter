from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Add image")


my_img = ImageTk.PhotoImage(Image.open("Screenshot.png"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root,text="Exit Program", command=root.destroy)
button_quit.pack()




root.mainloop()
     
