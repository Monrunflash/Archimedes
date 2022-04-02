#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import pygame
import time

root = Tk()
root.title("Hola")
root.geometry("500x400")

pygame.mixer.init()

def play():
    for s in text:
        print(s)
        if s != " ":
            pygame.mixer.music.load(f"Audacity/{s}.mp3")
            pygame.mixer.music.play(loops=0)
            time.sleep(0.28)
        else:
            time.sleep(0.3)

text = ["to","to","ro"," ","mi"," ","pe","li","cu","la"," ","fa","vo","ri","ta"]
my_button = Button(root, text="Play Audio", command=play)
my_button.pack(pady=20)

root.mainloop()
