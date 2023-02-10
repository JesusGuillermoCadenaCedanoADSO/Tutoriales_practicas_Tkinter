# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# # FreeCodeCamp.org
# # https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34
#
# # Message Boxes

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('E:/PycharmProjects/imagenes/file_type_python_icon_130221.ico')

# types of mesageboxes:
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno


def popup():
    response = messagebox.askokcancel("This is my Popup!", "Hello World!")
    Label(root, text=response).pack()
    # if response == 1:
    #     Label(root, text="You Clicked Yes!").pack()
    # else:
    #     Label(root, text="You Clicked No!").pack()


myButton = Button(root, text="Popup", command=popup)

myButton.pack()
root.mainloop()
