# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34

# Build a weather app
# https://docs.airnowapi.org/

from tkinter import *
import requests
import json


root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('E:/PycharmProjects/imagenes/file_type_python_icon_130221.ico')
root.geometry("400x40")
root.configure(background="green")

city = ""
quality = ""
category = ""

try:
    api_request = requests.get(
        "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=E02E857A-F374-4235-B92D-95A924AD798B")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']

except Exception as e:
    api = "Error..."

myLabel = Label(root,text=city + " Air Quality " + str(quality)+ " " + category, font=("Helvetica", 20),background="green")
myLabel.pack()


root.mainloop()

