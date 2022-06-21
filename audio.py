import pygame
import time
import os

pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)

arr = ["ra","re","ri","ro","ru"]

def play(textToPlay):
    for words in textToPlay:
        time.sleep(0.35)
        try:
            if words[0] in arr:
                r = "r" + words[0]
                words[0] = r
        except IndexError:
            pass
        for syll in words:
            print(syll)
            path = f"Audacity/{syll}.mp3"
            if os.path.isfile(path):
                pygame.mixer.music.load(path)
                pygame.mixer.music.play(loops=0)
                time.sleep(0.32)

def playEnglish(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(loops=0)
