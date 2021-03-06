#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import convert_text as ct

#patrones de vocales y consonantes y una serie de palabras habituales para crear
#una sintesis más realista
vocales = ["a","e","i","o","u"]
tonica = ["á","é","í","ó","ú"]
consonantes = ["b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z"]
numbers = {"uno":"1","dos":"2","tres":"3","cuatro":"4","cinco":"5","seis":"6"\
,"siete":"7","ocho":"8","nueve":"9"}
pronouns1 = ["que","cuando","como","donde","cual","cuales","cuanto","cuantos"]
pronouns2 = ["vosotros","nosotros","ellos","ellas"]
courtesy = ["hola","adios","gracias"]
ar = ["ra","re","ri","ro","ru"]
q = ["e","i"]

#creación de la estructura principal del patrón de separación según exista combinaciones
#de vocales y consonantes. Por ejemplo: una "consonante" y una "vocal" siempre formarán
#una sílaba junta. En cambio, dos "c" formarán sílabas diferentes
combination11 = ["v"]
combination12 = ["c"]
combination21 = ["v","c"]
combination22 = ["c","v"]
combination23 = ["c","c"]
combination24 = ["v","v"]
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

#función que separa las palabras y las mete en una variable de tipo realista
#esta función pasará cada palabra a la función que separa las palabras de los signos
def analizer(t):
    wordSeparated = list()
    wordSeparated = t.split()
    text = list()
    for wordToTest in wordSeparated:
        segment = ct.punctuation_separator(wordToTest)
        if isinstance(segment, list):
            for p in segment:
                text.append(p)
        else:
            text.append(wordToTest)
    text[:] = [x for x in text if x != ""]
    return filter(text)

#función encargada de analizar la palabra y discernir las sílabas que la componen
#se caracteriza por ser resiliente y tenerse que aplicar filtros con excepciones
#ya que no es perfecta la separación que lleva a cabo
def filter(t):
    textFiltered = list()
    for w in t:
        syllable = list()
        distributionLetter = list()
        wordToTest = list()
        for char in w:
            #crea una variable nueva donde la palabra para a ser un conjunto de
            #"v" y "c" para realizar una comprobación más sencilla según los patrones
            #anotados arriba
            try:
                wordToTest.append(char)
                if char in vocales:
                    distributionLetter.append("v")
                if char in consonantes:
                    distributionLetter.append("c")
                if int(char) or int(char) == 0:
                    distributionLetter.append("n")
                if char not in vocales and char not in consonantes and int(char) not in range(0,10):
                    distributionLetter.append("other")
            except ValueError:
                pass
        if "other" in distributionLetter:
            textFiltered.append(char)
        elif "n" in distributionLetter:
            textFiltered.append(w)
        else:
            distLenght = len(distributionLetter)
            while distLenght > 0:
                if distLenght == 1:
                    syllable.append(wordToTest[0])
                    distLenght -= 1
                if distLenght == 2:
                    charToProve = [distributionLetter[0],distributionLetter[1]]
                    if charToProve == combination21:
                        syllable.append("".join((wordToTest[0],wordToTest[1])))
                        distLenght -= 2
                    if charToProve == combination22:
                        syllable.append("".join((wordToTest[0],wordToTest[1])))
                        distLenght -= 2
                    if charToProve == combination23 or charToProve == combination24:
                        syllable.append(wordToTest[0])
                        syllable.append(wordToTest[1])
                        distLenght -= 2
                if distLenght == 3:
                    charToProve = [distributionLetter[0],distributionLetter[1],distributionLetter[2]]
                    if charToProve == combination31:
                        syllable.append(wordToTest[0])
                        syllable.append(wordToTest[1])
                        syllable.append(wordToTest[2])
                        distLenght -= 3
                    if charToProve == combination32:
                        syllable.append(wordToTest[0])
                        syllable.append("".join((wordToTest[1],wordToTest[2])))
                        distLenght -= 3
                    if charToProve == combination33:
                        syllable.append(wordToTest[0])
                        syllable.append("".join((wordToTest[1],wordToTest[2])))
                        distLenght -= 3
                    if charToProve == combination34:
                        syllable.append("".join((wordToTest[0],wordToTest[1])))
                        syllable.append(wordToTest[2])
                        distLenght -= 3
                    if charToProve == combination35:
                        syllable.append("".join((wordToTest[0],wordToTest[1])))
                        syllable.append(wordToTest[2])
                        distLenght -= 3
                    if charToProve == combination36:
                        syllable.append("".join((wordToTest[0],wordToTest[1])))
                        textFiltered.append(syllable)
                        syllable = list()
                        syllable.append("".join((wordToTest[1],wordToTest[2])))
                        distLenght -= 3
                    if charToProve == combination37:
                        syllable.append(wordToTest[0])
                        syllable.append("".join((wordToTest[1],wordToTest[2])))
                        distLenght -= 3
                    if charToProve == combination38:
                        syllable.append(wordToTest[0])
                        syllable.append(wordToTest[1])
                        syllable.append(wordToTest[2])
                        distLenght -= 3
                if distLenght > 3:
                    charToProve = [distributionLetter[0],distributionLetter[1],distributionLetter[2],distributionLetter[3]]
                    if charToProve == combination41:
                        syllable.append(wordToTest[0])
                        syllable.append(wordToTest[1])
                        syllable.append(wordToTest[2])
                        del(wordToTest[0:3])
                        del(distributionLetter[0:3])
                        distLenght -= 3
                    if charToProve == combination42:
                        syllable.append(wordToTest[0])
                        syllable.append(wordToTest[1])
                        del(wordToTest[0:2])
                        del(distributionLetter[0:2])
                        distLenght -= 2
                    if charToProve == combination43:
                        syllable.append(wordToTest[0])
                        del(wordToTest[0])
                        del(distributionLetter[0])
                        distLenght -= 1
                    if charToProve == combination44:
                        syllable.append(wordToTest[0])
                        syllable.append("".join((wordToTest[1],wordToTest[2])))
                        del(wordToTest[0:3])
                        del(distributionLetter[0:3])
                        distLenght -= 3
                    if charToProve == combination45:
                        syllable.append(wordToTest[0])
                        syllable.append("".join((wordToTest[1],wordToTest[2])))
                        del(wordToTest[0:3])
                        del(distributionLetter[0:3])
                        distLenght -= 3
                    if charToProve == combination46:
                        syllable.append(wordToTest[0])
                        del(wordToTest[0])
                        del(distributionLetter[0])
                        distLenght -= 1
                    if charToProve == combination47:
                        syllable.append("".join((wordToTest[0],wordToTest[1])))
                        del(wordToTest[0:2])
                        del(distributionLetter[0:2])
                        distLenght -= 2
                    if charToProve == combination48:
                        syllable.append("".join((wordToTest[0],wordToTest[1])))
                        syllable.append(wordToTest[2])
                        del(wordToTest[0:3])
                        del(distributionLetter[0:3])
                        distLenght -= 3
                    if charToProve == combination49:
                        syllable.append("".join((wordToTest[0],wordToTest[1])))
                        syllable.append(wordToTest[2])
                        del(wordToTest[0:3])
                        del(distributionLetter[0:3])
                        distLenght -= 3
                    if charToProve == combination410:
                        syllable.append("".join((wordToTest[0],wordToTest[1])))
                        del(wordToTest[0:2])
                        del(distributionLetter[0:2])
                        distLenght -= 2
                    if charToProve == combination411:
                        syllable.append("".join((wordToTest[0],wordToTest[1])))
                        del(wordToTest[0:2])
                        del(distributionLetter[0:2])
                        distLenght -= 2
                    if charToProve == combination412:
                        syllable.append("".join((wordToTest[0],wordToTest[1])))
                        textFiltered.append(syllable)
                        syllable = list()
                        syllable.append("".join((wordToTest[1],wordToTest[2])))
                        del(wordToTest[0:3])
                        del(distributionLetter[0:3])
                        distLenght -= 3
                    if charToProve == combination413:
                        syllable.append(wordToTest[0])
                        syllable.append("".join((wordToTest[1],wordToTest[2])))
                        del(wordToTest[0:3])
                        del(distributionLetter[0:3])
                        distLenght -= 3
                    if charToProve == combination414:
                        syllable.append(wordToTest[0])
                        del(wordToTest[0])
                        del(distributionLetter[0])
                        distLenght -= 1
                    if charToProve == combination415:
                        syllable.append(wordToTest[0])
                        syllable.append(wordToTest[1])
                        del(wordToTest[0:2])
                        del(distributionLetter[0:2])
                        distLenght -= 2
                    if charToProve == combination416:
                        syllable.append(wordToTest[0])
                        syllable.append(wordToTest[1])
                        syllable.append(wordToTest[2])
                        del(wordToTest[0:3])
                        del(distributionLetter[0:3])
                        distLenght -= 3
            textFiltered.append(syllable)
    return textFiltered

#función en la que suceden los filtros de excepciones, como el filtro que une
#["qu","e"] en una sola palabra o une ["ho","la"] ya que está palabra está grabada
#tal cual, porque es de un uso muy habitual.
def last_filter(t):
    reviewedText = list()
    for word in t:
        word = ar_sound(word)
        word = qu_sound(word)
        word = gu_sound(word)
        wordJoined = "".join(word)
        if wordJoined in numbers:
            reviewedText.append(numbers.get(wordJoined))
        elif wordJoined in pronouns1:
            w = [wordJoined]
            reviewedText.append(w)
        elif wordJoined in pronouns2:
            w = [wordJoined]
            reviewedText.append(w)
        elif wordJoined in courtesy:
            w = [wordJoined]
            reviewedText.append(w)
        else:
            reviewedText.append(word)
    return reviewedText

#función que comprueba si hay una r en medio de dos sílabas y las une
def ar_sound(w):
    newText = list()
    i = 0
    syll = str()
    lenght = len(w)
    while i < lenght:
        if w[i] in consonantes:
            if i < (lenght):
                try:
                    if w[i+1] in ar:
                        syll = w[i] + w[i+1]
                        newText.append(syll)
                        i += 1
                    else:
                        newText.append(w[i])
                except IndexError:
                    pass
        else:
            newText.append(w[i])
        i += 1
    return newText

#función que comprueba si la sílaba es un "que" o un "qui"
def qu_sound(w):
    newText = list()
    i = 0
    syll = str()
    lenght = len(w)
    while i < lenght:
        if w[i] == "qu":
            if i < (lenght):
                try:
                    if w[i+1] in q:
                        syll = w[i] + w[i+1]
                        newText.append(syll)
                        i += 1
                    else:
                        newText.append(w[i])
                except IndexError:
                    pass
        else:
            newText.append(w[i])
        i += 1
    return newText

#función que comprueba "gue" o "gui"
def gu_sound(w):
    newText = list()
    i = 0
    syll = str()
    lenght = len(w)
    while i < lenght:
        if w[i] == "gu":
            if i < (lenght):
                try:
                    if w[i+1] in q:
                        syll = w[i] + w[i+1]
                        newText.append(syll)
                        i += 1
                    else:
                        newText.append(w[i])
                except IndexError:
                    pass
        else:
            newText.append(w[i])
        i += 1
    return newText
