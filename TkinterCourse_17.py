# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34

#  Using databases

from tkinter import *
import sqlite3

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('E:/PycharmProjects/imagenes/file_type_python_icon_130221.ico')
root.geometry("400x600")

# create a database or connect to one

conn = sqlite3.connect('address_book.db')

# create cursor
c = conn.cursor()

# create table
c.execute("""
            CREATE TABLE addresses (
            first_name text,
            last_name text,
            address text,
            city text,
            state text,
            zipcode integer
            )
""")


# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()