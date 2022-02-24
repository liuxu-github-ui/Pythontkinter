from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog


#first windows
root = Tk()
root.title("first window")




def open():
    global my_image #becuase image will be put in the root windows box, we need to put it as global
    root.filename=filedialog.askopenfilename(initialdir="C:/",title="Select A file",filetypes=(("png files","*.png"),("csv files","*.csv")))
    my_label=Label(root,text=root.filename).pack()
   #put selected image to the GUI
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label=Label(image=my_image).pack()

    

my_btn=Button(root,text="Open File",command=open).pack()


root.mainloop()
     
