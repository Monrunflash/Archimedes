from tkinter import *
import pygame
import time

pygame.mixer.init()

def play(textToPlay):
    for words in textToPlay:
        for syll in words:
            print(syll)
            pygame.mixer.music.load(f"Audacity/{syll}.mp3")
            pygame.mixer.music.play(loops=0)
            time.sleep(0.35)
