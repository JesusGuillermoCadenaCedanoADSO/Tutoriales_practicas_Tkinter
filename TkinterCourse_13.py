# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34

#  Open Files Dialog Box

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('E:/PycharmProjects/imagenes/file_type_python_icon_130221.ico')

# root.filename = filedialog.askopenfilename(initialdir="E:/PycharmProjects/imagenes", title="Select a file",
#                                            filetypes=(("png files", "*.png"),("all files","*.*")))
# my_label = Label(root, text=root.filename).pack()
# my_image = ImageTk.PhotoImage(Image.open(root.filename))
# my_image_label = Label(image=my_image).pack()

global my_image


def open_image():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="E:/PycharmProjects/imagenes", title="Select a file",
                                               filetypes=(("png files", "*.png"),("all files","*.*")))
    my_label = Label(root, text=root.filename)
    my_label.pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image)
    my_image_label.pack()


my_btn = Button(root,text="Open File", command=open_image).pack()


root.mainloop()

