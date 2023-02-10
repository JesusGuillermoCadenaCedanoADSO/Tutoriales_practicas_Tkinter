# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34

#Intro to tkinter

from tkinter import *

root = Tk()
# creating a label widget
myLabel= Label(root, text="Hello world")
# shoving it onto the screen
myLabel.pack()

root.mainloop()
