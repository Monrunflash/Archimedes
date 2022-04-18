import pygame
import time
import os

pygame.mixer.init()

def play(textToPlay):
    for words in textToPlay:
        time.sleep(0.28)
        for syll in words:
            path = f"Audacity/{syll}.mp3"
            if os.path.isfile(path):
                pygame.mixer.music.load(path)
                pygame.mixer.music.play(loops=0)
                time.sleep(0.28)
