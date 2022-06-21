#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import word_analizer as wa
#patrones de signos para aplicar la normalización del texto
patternText = "[a-zA-Z0-9]|[á-úÁ-Ú]| |,|;|\.|:|\(|\)|\¿|\?|\¡|\!"
patternPunctuation = ",|;|\.|:|\(|\)|\¿|\?|\¡|\!"
patternWord = "[a-zA-Z0-9]|[á-úÁ-Ú]"

#función por la que pasa el texto y es separado y filtrado según pertenezca a
#signos permitidos o signos prohibidos
def convert(t):
    cleanText = str()
    for char in t:
        if(re.search(patternText, char)):
            char = char.lower()
            cleanText += char
    cleanText = wa.analizer(cleanText)
    return cleanText

#función para separar la palabra que tenga un signo de puntuación unido a ella
#por ejemplo: ["hola."], donde deberiamos separar el "hola" del "."
def punctuation_separator(w):
    if (re.search(patternPunctuation, w)):
        wordInList = list()
        wordInList = list(w)
        wordInList.append("*")
        lenghtOfList = len(wordInList) - 1
        i = 0
        wordStuck = str()
        wordsAndPunctuation = list()
        while i < lenghtOfList:
            while (re.search(patternPunctuation, wordInList[i])):
                wordsAndPunctuation.append(wordInList[i])
                i += 1
            while (re.search(patternWord, wordInList[i])):
                wordStuck += wordInList[i]
                i += 1
            else:
                wordsAndPunctuation.append(wordStuck)
                wordStuck = ""
        i += 1
        return wordsAndPunctuation
    else:
        return w
