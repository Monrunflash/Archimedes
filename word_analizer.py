#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import convert_text as ct

vocales = ["a","e","i","o","u"]
tonica = ["á","é","í","ó","ú"]
consonantes = ["b","c","d","f","g","h","i","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]

combination11 = ["v"]
combination21 = ["v","c"]
combination22 = ["c","v"]
combination31 = ["v","v","v"]
combination32 = ["v","v","c"]
combination33 = ["v","c","v"]
combination34 = ["v","c","c"]
combination35 = ["c","v","v"]
combination36 = ["c","v","c"]
combination37 = ["c","c","v"]
combination38 = ["c","c","c"]
combination41 = ["v","v","v","v"]
combination42 = ["v","v","v","c"]
combination43 = ["v","v","c","v"]
combination44 = ["v","v","c","c"]
combination45 = ["v","c","v","v"]
combination46 = ["v","c","v","c"]
combination47 = ["v","c","c","v"]
combination48 = ["v","c","c","c"]
combination49 = ["c","v","v","v"]
combination410 = ["c","v","v","c"]
combination411 = ["c","v","c","v"]
combination412 = ["c","v","c","c"]
combination413 = ["c","c","v","v"]
combination414 = ["c","c","v","c"]
combination415 = ["c","c","c","v"]
combination416 = ["c","c","c","c"]


def analizer(t):
    wordSeparated = list()
    wordSeparated = t.split()
    text = list()
    for w in wordSeparated:
        segment = ct.punctuation_separator(w)
        if isinstance(segment, list):
            for p in segment:
                text.append(p)
        else:
            text.append(w)
    text[:] = [x for x in text if x != ""]
    filter(text)

def filter(t):
    for w in t:
        syllable = str()
        distribution = list()
        for char in w:
            if char in vocales:
                distribution.append("v")
            if char in consonantes:
                distribution.append("c")
            if char not in vocales and char not in consonantes:
                distribution.append("other")
        if "other" in distribution:

        else:
            distLenght = len(distribution)
            while distLenght <= 0:
                if distLenght == 1:
                    syllable.append([distribution[0])
                    distLenght -= 1
                if distLenght == 2:
                    charToProve = [distribution[0],distribution[1]]
                    if charToProve == combination21:
                        syllable.append(charToProve)
                        distLenght -= 2
                    if charToProve == combination22:
                        syllable.append(charToProve)
                        distLenght -= 2
                    else:
                        syllable.append(distribution[0])
                        syllable.append(distribution[1])
                        distLenght -= 2
                if distLenght == 3:
                    charToProve = [distribution[0],distribution[1],distribution[2]]
                    if charToProve == combination31:
                        syllable.append(distribution[0])
                        syllable.append(distribution[1])
                        syllable.append(distribution[2])
                        distLenght -= 3
                    if charToProve == combination32:
                        syllable.append(distribution[0])
                        syllable.append(distribution[1],distribution[2])
                        distLenght -= 3
                    if charToProve == combination33:
                        syllable.append(distribution[0])
                        syllable.append(distribution[1],distribution[2])
                        distLenght -= 3
                    if charToProve == combination34:
                        syllable.append(distribution[0],distribution[1])
                        syllable.append(distribution[2])
                        distLenght -= 3
                    if charToProve == combination35:
                        syllable.append(distribution[0],distribution[1])
                        syllable.append(distribution[2])
                        distLenght -= 3
                    if charToProve == combination36:
                        syllable.append(charToProve)
                        distLenght -= 3
                    if charToProve == combination37:
                        syllable.append(distribution[0])
                        syllable.append(distribution[1],distribution[2])
                        distLenght -= 3
                    if charToProve == combination38:
                        syllable.append(distribution[0])
                        syllable.append(distribution[1])
                        syllable.append(distribution[2])
                        distLenght -= 3
                if distLenght > 3:
                    charToProve = [distribution[0],distribution[1],distribution[2],distribution[3]]
                    if charToProve == combination41:
                        a
                    if charToProve == combination42:
                        a
                    if charToProve == combination43:
                        a
                    if charToProve == combination44:
                        a
                    if charToProve == combination45:
                        a
                    if charToProve == combination46:
                        a
                    if charToProve == combination47:
                        a
                    if charToProve == combination48:
                        a
                    if charToProve == combination49:
                        a
                    if charToProve == combination410:
                        a
                    if charToProve == combination411:
                        a
                    if charToProve == combination412:
                        a
                    if charToProve == combination413:
                        a
                    if charToProve == combination414:
                        a
                    if charToProve == combination415:
                        a
                    if charToProve == combination416:
                        a
