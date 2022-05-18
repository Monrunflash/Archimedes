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
        [
        sg.Text("Resolución = "),
        sg.Combo(["200,200","300,300","400,400","500,500","600,600","700,700","800,800"],default_value="200,200",key="-RESOLUTION-"),
        sg.Text("Tamaño de letra = "),
        sg.InputText(key="-FONT_SIZE-"),
        sg.Text("Estilo de letra = "),
        sg.Combo(["Courier New","Times New Roman","Arial","Lucida"],default_value="Courier New",key="-FONT_STYLE-"),
        sg.Text("Color de la interfaz = "),
        sg.Combo(["Azul","Rojo","Verde"],default_value="Azul",key="-COLOR-"),
        sg.Button("Enviar Configuración")
        ]
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
    [
    sg.Text("Input text:"),
    sg.Multiline(size=(40,20), font=(c[2],c[1]), enable_events=True, key="-INPUT-"),
    sg.Button("Enviar")
    ]
    ]

    text_output = [
    [sg.Text("Clear Text:")],
    [sg.Text(size=(40,20), key="-OUTPUT-")],
    [sg.Image(key="-IMAGE-")],
    ]

    layout = [
    [
    sg.Column(text_input),
    sg.VSeparator(),
    sg.Column(text_output),
    ]
    ]

    return sg.Window("Archimedes", layout, finalize=True)

valuesOfConfiguration = read_file()
window = established_cofig(valuesOfConfiguration)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Enviar":
        text = values["-INPUT-"]
        text = ct.convert(text)
        window["-OUTPUT-"].update(text)
        text = wa.last_filter(text)
        print(text)
        audio.play(text)
    if event == "Enviar Configuración":
        configToSave = list()
        configToSave = [values["-RESOLUTION-"],values["-FONT_SIZE-"],values["-FONT_STYLE-"],values["-COLOR-"]]
        print(configToSave)
        save_config(configToSave)
        established_cofig(configToSave)
        read_file()

window.close()
