# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34

#  Sliders

from tkinter import *

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('E:/PycharmProjects/imagenes/file_type_python_icon_130221.ico')
root.geometry("400x400")

vertical = Scale(root, from_=0,to=400)
vertical.pack()


def slide():
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))


horizontal = Scale(root, from_=0,to=400, orient=HORIZONTAL)
horizontal.pack()

my_label= Label(root,text=horizontal.get()).pack()


my_btn = Button(root, text="Click me!", command=slide).pack()


root.mainloop()

