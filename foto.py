import PySimpleGUI as sg
import time

imager_viewer_column = [[
    sg.Text("Display"),
    sg.Image(size=(450,500),filename="bocacerrada.png",key="-IMG-"),
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
        print(i)
        while i < 5:
            window["-IMG-"].update(size=(450,500),filename="bocabierta.png")
            window.read(timeout=100)
            print("abierta")
            time.sleep(0.3)
            window["-IMG-"].update(size=(450,500),filename="bocacerrada.png")
            window.read(timeout=100)
            print("cerrada")
            i+=1
