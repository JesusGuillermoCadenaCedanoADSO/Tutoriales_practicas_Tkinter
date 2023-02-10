# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34

# Addin Frames To Your Program

from tkinter import *

root = Tk()

frame = LabelFrame(root,text="This is my Frame...", padx=5,pady=5)
frame.pack(padx=100, pady=100)

b = Button(frame, text="Don't click here!")
# b.pack()
b.grid(row=0,column=0)

b2 = Button(frame, text="...or here!")
b2.grid(row=1,column=0)


root.mainloop()