# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34


# Using Icons, Images, and Exit Buttons

from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title()
root.iconbitmap('E:/PycharmProjects/imagenes/file_type_python_icon_130221.ico')

my_img = ImageTk.PhotoImage(Image.open('E:/PycharmProjects/imagenes/planeta.jpg'))

my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()
root.mainloop()
