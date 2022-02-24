from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


#first windows
root = Tk()
root.title("first window")
root.geometry("400x400")#default windows size




#show the slider value

def slide(var):
    my_label=Label(root,text=horizontal.get()).pack()
    
#scal widget
vertical = Scale(root, from_=0, to=200)
vertical.pack()


horizontal = Scale(root, from_=0, to=200, orient= HORIZONTAL,command=slide)
horizontal.pack()







root.mainloop()
     
