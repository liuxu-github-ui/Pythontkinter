from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("radio button")


r = IntVar() # It allows tkinter keep track of which button has been clicked
r.set("2")

MODES=[
    ("option1","option1"),
    ("option2","option2"),
    ("option3","option3"),
    ("option4","option4"),
]

pizza=StringVar()

pizza.set("option1")

for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza, value=mode).pack(anchor=W)



def clicked(value):
    myLabel = Label(root,text=value)
    myLabel.pack()

    

#Radiobutton(root,text="Option 1", variable=r, value=1,command= lambda: clicked(r.get())).pack()
#Radiobutton(root,text="Option 2", variable=r, value=2,command= lambda: clicked(r.get())).pack()


#myLabel = Label(root,text=pizza.get())
#myLabel.pack()

myButton = Button(root,text="Click Me", command= lambda: clicked(pizza.get()))
myButton.pack()



root.mainloop()
     
