from tkinter import *
from PIL import ImageTk,Image
import sqlite3


#first windows
root = Tk()
root.title("first window")
root.geometry("400x400")#default windows size


# connect database or create a database

conn = sqlite3.connect('address_book.db') # it will create a addre_book.db file in local dir

#create cursor
c = conn.cursor()

#create table
c.execute("""CREATE TABLE addresses(
            first_name text,
            last_name  text,
            address    text,
            city       text,
            state      text,
            zipcode    integer) """)





#commit changes
conn.commit()

#close connection
conn.close()



root.mainloop()
     
