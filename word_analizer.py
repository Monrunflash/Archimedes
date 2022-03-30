#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import convert_text as ct

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
    return text
