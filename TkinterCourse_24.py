# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34

# Matplotlib Charts
# https://docs.airnowapi.org/

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('E:/PycharmProjects/imagenes/file_type_python_icon_130221.ico')


def graph():
    house_prices = np.random.normal(200000,25000,5000)
    plt.hist(house_prices, 50)
    plt.show()


my_button = Button(root, text="Graph It", command=graph)
my_button.pack()


root.mainloop()

