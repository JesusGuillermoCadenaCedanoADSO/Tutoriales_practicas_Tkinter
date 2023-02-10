# Tkinter Course - Create Graphic User Interfaces in Python Tutorial
# FreeCodeCamp.org
# https://www.youtube.com/watch?v=YXPyB4XeYLA&list=PLDobAhKPyFshFDhgbHQdPZ2oc2iBITPAl&index=34

# Add zip code lookup form
# https://docs.airnowapi.org/

from tkinter import *
import requests
import json


root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('E:/PycharmProjects/imagenes/file_type_python_icon_130221.ico')
root.geometry("600x100")

# Create Zipcode Lookup Function


def zipLookup():
    # zip_textbox.get()
    # zip_label = Label(root, text=zip_textbox.get())
    # zip_label.grid(row=1, column=0, columnspan=2)
    try:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip_textbox.get() + "&distance=25&API_KEY=E02E857A-F374-4235-B92D-95A924AD798B")
        api = json.loads(api_request.content)
        city = api[0]['ReportingArea']
        quality = api[0]['AQI']
        category = api[0]['Category']['Name']

        if category == "Good":
            weather_color = "#00e400"
        elif category == "Moderate":
            weather_color = "#ffff00"
        elif category == "Unhealthy for Sensitive Groups":
            weather_color = "#ff7e00"
        elif category == "Unhealthy":
            weather_color = "#ff0000"
        elif category == "Very Unhealthy":
            weather_color = "#8f3f97"
        elif category == "Hazardous":
            weather_color = "#7e0023"

        myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20),
                        background=weather_color)
        root.configure(background=weather_color)
        myLabel.grid(row=1,column=0,columnspan=2)

    except Exception as e:
        api = "Error..."

city = ""
quality = ""
category = ""

# try:
#     api_request = requests.get(
#         "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=83530&distance=25&API_KEY=E02E857A-F374-4235-B92D-95A924AD798B")
#     api = json.loads(api_request.content)
#     city = api[0]['ReportingArea']
#     quality = api[0]['AQI']
#     category = api[0]['Category']['Name']
#
#     if category == "Good":
#         weather_color = "#00e400"
#     elif category == "Moderate":
#         weather_color = "#ffff00"
#     elif category == "Unhealthy for Sensitive Groups":
#         weather_color = "#ff7e00"
#     elif category == "Unhealthy":
#         weather_color = "#ff0000"
#     elif category == "Very Unhealthy":
#         weather_color = "#8f3f97"
#     elif category == "Hazardous":
#         weather_color = "#7e0023"
#
#     myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvetica", 20),
#                     background=weather_color)
#     myLabel.pack()
#
# except Exception as e:
#     api = "Error..."


zip_textbox = Entry(root)
zip_textbox.grid(row=0,column=0, stick=W+E+N+S)

zipButton = Button(root,text="Lookup Zipcode", command=zipLookup)
zipButton.grid(row=0,column=1, stick=W+E+N+S)

root.mainloop()

