#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 17:04:52 2024

@author: drasken
"""

#FUNCRION NOT WORING SOMETIMES INFINITE LOOP
def getNumberFromString(stringa:str) -> str:
    """ Given a string in wich there is a nuber return the first number found"""
    
    for index, char in enumerate(stringa):
        if char.isdigit():
            stringa[index:]
            step = 1
            while stringa[index: index + step].isdigit():
                step +=1
            return stringa[index: index + step]
    
    return '' #if no number is found


def extractNumberForColor(stringa):
    """
    check if substring of desired colors appear and than find the number preceding it 

    Parameters
    ----------
    stringa : TYPE
        The string from wich extract numbers.

    Returns
    -------
    dictColors: a dict of boolean, if all true the game is ok

    """
    
    listColors = ['red', 'green', 'blue']
    
    for color in listColors:
        stringa.find(color)
    
    dictColors = {}
    return dictColors