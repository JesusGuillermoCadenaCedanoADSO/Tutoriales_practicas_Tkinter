# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34

# Radio Buttons

from tkinter import *

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('E:/PycharmProjects/imagenes/file_type_python_icon_130221.ico')

# r = IntVar()
# r.set("2")

TOPPINGS = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion")
]


pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root,text=text, variable=pizza,value=topping).pack(anchor=W)


def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()


# Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda:clicked(r.get())).pack()
# Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda:clicked(r.get())).pack()


# myLabel = Label(root,text=r.get())

# myLabel = Label(root,text=pizza.get())
# myLabel.pack()

# myButton = Button(root, text="Click Me!",command=lambda:clicked(r.get()))
myButton = Button(root, text="Click Me!", command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()

