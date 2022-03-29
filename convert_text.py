#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

pattern = "[a-zA-Z0-9]|[á-ú-Á-Ú]| |,|;|\.|:|\(|\)|\¿|\?|\¡|\!|\-"

def convert(t):
    cleanText = str()
    for char in t:
        if(re.search(pattern, char)):
            char = char.lower()
            cleanText += char
    return cleanText
