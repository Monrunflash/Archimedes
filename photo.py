import PySimpleGUI as sg
import time
from PIL import Image

imager_viewer_column = [[
    sg.Text("Display"),
    sg.Image(filename="buho_m6.png",key="-IMG-"),
    sg.Button("Enviar")
]]

layout = [
    [
        sg.Column(imager_viewer_column)
    ]
]

window = sg.Window("Imagen", layout)


while True:
    event, values = window.read(timeout=100)
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Enviar":
        i = 0
        window.read(timeout=100)
        while i < 5:
            window["-IMG-"].update(filename="buho_m2.png")
            window.read(timeout=100)
            print("abierta")
            time.sleep(0.4)
            window["-IMG-"].update(filename="buho_m3.png")
            window.read(timeout=100)
            print("cerrada")
            i+=1
            if i == 5:
                window["-IMG-"].update(filename="buho_m4.png")
                window.read(timeout=100)
                time.sleep(0.6)
                window["-IMG-"].update(filename="buho_m5.png")
                window.read(timeout=100)
