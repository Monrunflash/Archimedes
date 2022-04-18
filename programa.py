#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import PySimpleGUI as sg
import os.path
import convert_text as ct
import audio2 as audio
from tkinter import *
import pygame
import time

sg.theme('Reddit')
text_input = [
    [
        sg.Text("Input text:"),
        sg.Multiline(size=(40,20), font=('Courier New',12), enable_events=True, key="-INPUT-"),
        sg.Button("SENT")
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

window = sg.Window("Archimedes", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "SENT":
        text = values["-INPUT-"]
        text = ct.convert(text)
        window["-OUTPUT-"].update(text)
        audio.play(text)

window.close()
