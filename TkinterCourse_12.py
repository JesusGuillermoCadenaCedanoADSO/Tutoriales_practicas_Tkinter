# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34

# Create New Windows in tKinter

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('E:/PycharmProjects/imagenes/file_type_python_icon_130221.ico')
global my_img


def open_window():
    global my_img
    top = Toplevel()
    top.title('My second window')
    top.iconbitmap('E:/PycharmProjects/imagenes/file_type_python_icon_130221.ico')

    my_img = ImageTk.PhotoImage(Image.open("imagenes/Plomombia.png"))
    my_label = Label(top, image=my_img)
    my_label.pack()
    btn2 = Button(top,text="close window",command=top.destroy)
    btn2.pack()


btn = Button(root, text="Open Second Window", command=open_window).pack()


# lbl = Label(top, text="Hellow World").pack()



root.mainloop()