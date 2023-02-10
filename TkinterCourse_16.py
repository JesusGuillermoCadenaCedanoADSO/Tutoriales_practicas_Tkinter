# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34

#  Dropdown Menus

from tkinter import *

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('E:/PycharmProjects/imagenes/file_type_python_icon_130221.ico')
root.geometry("400x400")


def show():
    myLabel= Label(root,text=clicked.get()).pack()


options = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root,clicked, *options)
drop.pack()

myButton = Button(root,text="Show selection",command=show).pack()

root.mainloop()