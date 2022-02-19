from tkinter import *


root = Tk()

#entry widge (inputfield)
e= Entry(root)
e.pack()


def myClick():
    myLabel= Label(root,text=e.get())
    myLabel.pack()

#create a button widget
myButton = Button(root,text="Enter something",command=myClick, fg="blue")

myButton.pack()

root.mainloop()
     
