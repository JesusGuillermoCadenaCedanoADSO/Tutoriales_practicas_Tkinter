# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34

# Creating Buttons

from tkinter import *

root = Tk()

def myClick():
    myLabel=Label(root,text="Look! I clicked a Button!")
    myLabel.pack()

# myButton = Button(root,text="Click Me!",state=DISABLED,padx=50,pady=50)
myButton = Button(root,text="Click Me!",command=myClick,fg="green", bg="yellow")
myButton.pack()

root.mainloop()

