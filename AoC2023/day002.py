#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 00:05:29 2024

@author: drasken
"""
"""
Determine which games would have been possible if the bag had been loaded with 
only 12 red cubes, 13 green cubes, and 14 blue cubes.
What is the sum of the IDs of those games?
"""

"""
Possibile idee per calcolare analizzare le stringhe:
    prendi la stringa sa sopo i 2 punti
    prendi ogni set usando cone separatore il punto e virgola
    prendi come separatore le virgole
    dovrebbe essermi rimaste tutte substring del tipo --23 Colore--
    cerco di estrarre il numero dalla stringa(modulo da importare??)
    check con le condizione dell'indovinello
    se ok aggiungi 1 al counter
    ritorna counter
    

"""

import stringFunction


def readInput(inputFile):
    
    """"using this generator to read the file"""
    
    with open(inputFile, mode='r') as f:
        context = f.readlines() #read file each str is a game
        for line in context:
            yield line #yield the str corrisponding on the line
           
            


if __name__ == '__main__':
    #need to process this names
    cubesOfGmes = '12 red cubes, 13 green cubes, and 14 blue cubes'

    fileInput = 'input002.txt'
    provaReadFile = readInput('input002.txt')
    provaGen = next(provaReadFile)
    provaGen2 = next(provaReadFile)
    provaSplit = provaGen2.split(';')
    

    