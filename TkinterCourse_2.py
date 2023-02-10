# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34

# Positioning With Tkinter's Grid System

from tkinter import *

root = Tk()
myLabel1 = Label(root, text="Hello World!").grid(row=0,column=0)
myLabel2 = Label(root, text="mi nombre es jesus").grid(row=1,column=1)

# myLabel1.grid(row=0,column=0)
# myLabel2.grid(row=1,column=1)

root.mainloop()








