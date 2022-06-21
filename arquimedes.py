#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
from tkinter import *
import pygame
import time
import os.path
import convert_text as ct
import word_analizer as wa
import audio
from gtts import gTTS

def read_file():
    if os.path.isfile("config.txt"):
        file = open("config.txt","r")
        confValues = list()
        for line in file.readlines():
            values = line.split("=")
            values[1] = values[1].replace("\n","")
            if values[0] == "first_config":
                if values[1] == "Yes":
                    file.close()
                    return True
            if values[0] == "resolution":
                confValues.append(values[1])
            if values[0] == "font_size":
                confValues.append(values[1])
            if values[0] == "font_style":
                confValues.append(values[1])
            if values[0] == "color":
                confValues.append(values[1])
        file.close()
        return confValues
    else:
        file = open("config.txt","w+")
        file.close()
        return True

def save_config(c):
    file = open("config.txt","w+")
    reso = "resolution=" + c[0] + "\n"
    size = "font_size=" + c[1] + "\n"
    style = "font_style=" + c[2] + "\n"
    color = "color=" +c[3] + "\n"
    file.write("first_config=No\n")
    file.write(reso)
    file.write(size)
    file.write(style)
    file.write(color)
    file.close()

def established_cofig(c):
    if c != True:
        return spanish_window(c)
    else:
        return configuration_window()

def configuration_window():
    config_menu = [
        [sg.Text("Resolución = ")],
        [sg.Combo(["Pequeña","Mediana","Grande"],default_value="Pequeña",key="-RESOLUTION-")],
        [sg.Text("Tamaño de letra = ")],
        [sg.Combo(["12","13","14","15","16"],default_value="12",key="-FONT_SIZE-")],
        [sg.Text("Estilo de letra = ")],
        [sg.Combo(["Courier New","Times New Roman","Arial","Lucida"],default_value="Courier New",key="-FONT_STYLE-")],
        [sg.Text("Color de la interfaz = ")],
        [sg.Combo(["Azul","Rojo","Verde"],default_value="Azul",key="-COLOR-")],
        [sg.Button("Enviar Configuración")]
    ]

    layout = [
    [
    sg.Column(config_menu),
    ]
    ]

    return sg.Window("Configuración", layout, finalize=True)

def spanish_window(c):
    if c[3] == "Azul":
        sg.theme('Reddit')
    if c[3] == "Rojo":
        sg.theme('DarkRed1')
    if c[3] == "Verde":
        sg.theme('GreenMono')
    text_input = [
    [sg.Combo(["Español","Inglés"],default_value="Español",key="-IDIOM-")],
    [sg.Text("Input text:"),
    sg.Multiline(size=(35,15), font=(c[2],c[1]), enable_events=True, key="-INPUT-")],
    [sg.Button("Enviar"), sg.Button("Config")]
    ]

    text_output = [
    [sg.Text("Clear Text:")],
    [sg.Text(size=(20,15), key="-OUTPUT-")],
    [sg.Image(filename="img/buho_m6.png",key="-IMG-")]
    ]

    layout = [
    [
    sg.Column(text_input,element_justification="c"),
    sg.VSeparator(),
    sg.Column(text_output,element_justification="c"),
    ]
    ]

    return sg.Window("Archimedes", layout, finalize=True)

valuesOfConfiguration = read_file()
if valuesOfConfiguration == True:
    window2, window1 = established_cofig(valuesOfConfiguration), None
else:
    window1, window2 = established_cofig(valuesOfConfiguration), None

while True:
    window, event, values = sg.read_all_windows()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Enviar":
        text = values["-INPUT-"]
        idiom = values["-IDIOM-"]
        print(idiom)
        if idiom == "Español":
            text = ct.convert(text)
            text = wa.last_filter(text)
            window["-OUTPUT-"].update(text)
            window.read(timeout=100)
            i = 0
            while i < 3:
                window["-IMG-"].update(filename="img/buho_m2.png")
                window.read(timeout=100)
                #print("abierta")
                time.sleep(0.4)
                window["-IMG-"].update(filename="img/buho_m3.png")
                window.read(timeout=100)
                #print("cerrada")
                i+=1
                if i == 3:
                    window["-IMG-"].update(filename="img/buho_m4.png")
                    window.read(timeout=100)
                    time.sleep(0.6)
                    window["-IMG-"].update(filename="img/buho_m5.png")
                    window.read(timeout=100)
                    audio.play(text)
        if idiom == "Inglés":
            language = "en"
            output = gTTS(text=text, lang=language, slow=False)
            output.save("output.mp3")
            audio.playEnglish("output.mp3")
            os.system("rm -f output.mp3")
    if event == "Enviar Configuración":
        configToSave = list()
        configToSave = [values["-RESOLUTION-"],values["-FONT_SIZE-"],values["-FONT_STYLE-"],values["-COLOR-"]]
        print(configToSave)
        save_config(configToSave)
        established_cofig(configToSave)
        read_file()
        window2.close()
    if event == "Config" and not window2:
        window2 = configuration_window()
        window1.close()
window.close()
