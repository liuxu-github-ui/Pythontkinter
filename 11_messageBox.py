from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


root = Tk()
root.title("message Box")


#Instead of using showinfor, we can also use showwarnning, showerror,askquestion,askokcancel,askyesno

def popup():
    response= messagebox.askyesno("This is popup","Hello")
    

    if response==1:
        Label(root,text="You click yes").pack() #show the user selection of the messagebox
    else:
        Label(root,text="You click no").pack() #show the user selection of the messagebox



Button(root,text="Popup",command=popup).pack()






root.mainloop()
     
