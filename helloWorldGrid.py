from tkinter import *


root = Tk()

def myClick():
    myLabel= Label(root,text="Look")
    myLabel.pack()

#create a button widget
myButton = Button(root,text="click Me!",command=myClick, fg="blue")

myButton.pack()

root.mainloop()
     
