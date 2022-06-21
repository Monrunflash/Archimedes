#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import time
import os

#inicia el mezclador de sonidos
pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)

arr = ["ra","re","ri","ro","ru"]

#función principal del reproductor. Recorre cada palabra del texto pasado como variable
#y luego recorre las silabas que componen a la palabra para reproducir sílaba por sílaba
#es resiliente ya que no existen apenas sílabas que no sea capaz de reproducir
def play(textToPlay):
    for words in textToPlay:
        time.sleep(0.35)
        try:
            if words[0] in arr:
                r = "r" + words[0]
                words[0] = r
        except IndexError:
            pass
        for syll in words: #función que recorre las silabas y la reproduce según el fichero de audio
            path = f"Audacity/{syll}.mp3"
            if os.path.isfile(path):
                pygame.mixer.music.load(path)
                pygame.mixer.music.play(loops=0)
                time.sleep(0.32)

#función dedicada al reproductor de audio en la versión en inglés
def playEnglish(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(loops=0)
