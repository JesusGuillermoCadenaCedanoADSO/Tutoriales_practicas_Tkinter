# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34


# Creating input Fields

from tkinter import *

root = Tk()

e = Entry(root, width=50, borderwidth=5)
e.pack()
e.insert(0,"Enter your name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel=Label(root,text=hello)
    myLabel.pack()

# myButton = Button(root,text="Click Me!",state=DISABLED,padx=50,pady=50)
myButton = Button(root,text="Enter your name",command=myClick,fg="white", bg="blue")
myButton.pack()

root.mainloop()