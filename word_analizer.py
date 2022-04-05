#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import convert_text as ct

vocales = ["a","e","i","o","u"]
tonica = ["á","é","í","ó","ú"]
consonantes = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]

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
    textFiltered = list()
    for w in t:
        syllable = list()
        distribution = list()
        for char in w:
            if char in vocales:
                distribution.append("v")
            if char in consonantes:
                print(char)
                distribution.append("c")
            if char not in vocales and char not in consonantes:
                distribution.append("other")
        if "other" in distribution:
            textFiltered.append(distribution)
        else:
            distLenght = len(distribution)
            print(distLenght)
            while distLenght > 0:
                print(distLenght)
                if distLenght == 1:
                    syllable.append(distribution[0])
                    distLenght -= 1
                if distLenght == 2:
                    charToProve = [distribution[0],distribution[1]]
                    if charToProve == combination21:
                        syllable.append("".join((distribution[0],distribution[1])))
                        distLenght -= 2
                    if charToProve == combination22:
                        syllable.append("".join((distribution[0],distribution[1])))
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
                        syllable.append("".join((distribution[1],distribution[2])))
                        distLenght -= 3
                    if charToProve == combination33:
                        syllable.append(distribution[0])
                        syllable.append("".join((distribution[1],distribution[2])))
                        distLenght -= 3
                    if charToProve == combination34:
                        syllable.append("".join((distribution[0],distribution[1])))
                        syllable.append(distribution[2])
                        distLenght -= 3
                    if charToProve == combination35:
                        syllable.append("".join((distribution[0],distribution[1])))
                        syllable.append(distribution[2])
                        distLenght -= 3
                    if charToProve == combination36:
                        syllable.append("".join((distribution[0],distribution[1],distribution[2])))
                        distLenght -= 3
                    if charToProve == combination37:
                        syllable.append(distribution[0])
                        syllable.append("".join((distribution[1],distribution[2])))
                        distLenght -= 3
                    if charToProve == combination38:
                        syllable.append(distribution[0])
                        syllable.append(distribution[1])
                        syllable.append(distribution[2])
                        distLenght -= 3
                if distLenght > 3:
                    charToProve = [distribution[0],distribution[1],distribution[2],distribution[3]]
                    if charToProve == combination41:
                        syllable.append(distribution[0])
                        syllable.append(distribution[1])
                        syllable.append(distribution[2])
                        del(distribution[0:3])
                        distLenght -= 3
                    if charToProve == combination42:
                        syllable.append(distribution[0])
                        syllable.append(distribution[1])
                        del(distribution[0:2])
                        distLenght -= 2
                    if charToProve == combination43:
                        syllable.append(distribution[0])
                        del(distribution[0])
                        distLenght -= 1
                    if charToProve == combination44:
                        syllable.append(distribution[0])
                        syllable.append("".join((distribution[1],distribution[2])))
                        del(distribution[0:3])
                        distLenght -= 3
                    if charToProve == combination45:
                        syllable.append(distribution[0])
                        syllable.append("".join((distribution[1],distribution[2])))
                        del(distribution[0:3])
                        distLenght -= 3
                    if charToProve == combination46:
                        syllable.append(distribution[0])
                        del(distribution[0])
                        distLenght -= 1
                    if charToProve == combination47:
                        print("7s")
                        syllable.append("".join((distribution[0],distribution[1])))
                        del(distribution[0:2])
                        distLenght -= 2
                    if charToProve == combination48:
                        syllable.append("".join((distribution[0],distribution[1])))
                        syllable.append(distribution[2])
                        del(distribution[0:3])
                        distLenght -= 3
                    if charToProve == combination49:
                        syllable.append("".join((distribution[0],distribution[1])))
                        syllable.append(distribution[2])
                        del(distribution[0:3])
                        distLenght -= 3
                    if charToProve == combination410:
                        syllable.append("".join((distribution[0],distribution[1])))
                        del(distribution[0:2])
                        distLenght -= 2
                    if charToProve == combination411:
                        syllable.append("".join((distribution[0],distribution[1])))
                        del(distribution[0:2])
                        distLenght -= 2
                    if charToProve == combination412:
                        syllable.append("".join((distribution[0],distribution[1],distribution[2])))
                        del(distribution[0:3])
                        distLenght -= 3
                    if charToProve == combination413:
                        syllable.append(distribution[0])
                        syllable.append("".join((distribution[1],distribution[2])))
                        del(distribution[0:3])
                        distLenght -= 3
                    if charToProve == combination414:
                        syllable.append(distribution[0])
                        del(distribution[0])
                        distLenght -= 1
                    if charToProve == combination415:
                        syllable.append(distribution[0])
                        syllable.append(distribution[1])
                        del(distribution[0:2])
                        distLenght -= 2
                    if charToProve == combination416:
                        syllable.append(distribution[0])
                        syllable.append(distribution[1])
                        syllable.append(distribution[2])
                        del(distribution[0:3])
                        distLenght -= 3
            textFiltered.append(syllable)
    print(textFiltered)
    return textFiltered
