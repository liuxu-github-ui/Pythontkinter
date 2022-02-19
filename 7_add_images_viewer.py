from tkinter import *
from PIL import ImageTk,Image


root = Tk()
root.title("Add image")


my_img = ImageTk.PhotoImage(Image.open("Screenshot.png"))
my_img2 = ImageTk.PhotoImage(Image.open("download.png"))

image_list=[my_img,my_img2]

my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3) # columnspan=3: make the image span across 3 buttons 


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget() # remove the current image before put the new one
    my_label=Label(image=image_list[image_number-1])
    button_forward = Button(root,text=">>",command=lambda: forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda: back(image_number-1))

    print(image_number)

#check whether in last image (in this case we only have 2 imges, so the number is 2), if yes, disalbe forward
    if image_number ==2:
        button_forward = Button(root,text=">>",state=DISABLED)
        

    
    my_label.grid(row=0, column=0, columnspan=3)

    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    

def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward = Button(root,text=">>",command=lambda: forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda: back(image_number-1))

    if image_number ==2:
        button_forward = Button(root,text=">>",state=DISABLED)    

    my_label.grid(row=0, column=0, columnspan=3)

    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)

    
    

button_back=Button(root,text="<<",command=back,state= DISABLED)
button_exit=Button(root,text="Exit Program",command=root.destroy)
button_forward=Button(root,text=">>", command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)




root.mainloop()
     
