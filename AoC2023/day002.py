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
 

def analyzeGames(fileName :str, colors: dict, colorsList: list) -> int:
    """ Analyze a game by each subset and if all true return the ID int
    
    """
    
    resIds = []
    powersIds = []
    
    fileReader = readInput(fileName)
    for linea in fileReader:
        processedLine = divideGameBySets(linea)
        processedLine = divideSetByCubes(processedLine) #here is divided list of list for each set
        isPlayable = checkIfPlayableGame(processedLine, colors)
        if isPlayable:
            gameId = linea[5: linea.index(':')]
            resIds.append(int(gameId))
            
        #here put calculatepowers functions
    
    return sum(resIds), sum(powersIds)
    pass

def divideGameBySets(gameString:str) -> list:
    
    gameString = gameString[gameString.index(':') + 2:]
    gameString = gameString.split(';')
    return gameString
    pass

def divideSetByCubes(setOfCubes: list[str]) -> list[list]:
    
    resList = [stringa.split(',') for stringa in setOfCubes]
    
    return resList
    pass

def getMinValue(listOfSets: list, listOfColors: list) -> dict:
    """Use this function on the set list, call it in another for the game list"""
    
    resDict = dict()
    
    for stringa in listOfSets:
        for colore in listOfColors:
            if colore in stringa:
                val = int(stringFunction.getNumberFromString(stringa))
                if colore not in resDict:
                    resDict[colore] = val
                else:
                    resDict[colore] = min(resDict[colore], val)
    
    return resDict
    
    pass
            
def checkIfPlayableSet(gamesAnalyzed: list, colors: dict) -> bool:
    
    setBoolRes = set()                
                    
    for stringa in gamesAnalyzed:
        for colore in colors:
            if colore in stringa:
                score = int(stringFunction.getNumberFromString(stringa))
                if score <= colors[colore]:
                    setBoolRes.add(True)
                else:
                    setBoolRes.add(False)
    
    return all(setBoolRes)
        
    pass

def checkIfPlayableGame (gameList: list, colors: dict) -> list[bool]:
    
    resSetBool = set()
    
    for miniList in gameList:
        getBool = checkIfPlayableSet(miniList, colors)
        resSetBool.add(getBool)
        
    return all(resSetBool)


if __name__ == '__main__':
    #need to process this names
    cubesOfGmes = {'red': 12, 'green': 13, 'blue': 14}
    colorsList = ['red', 'green', 'blue']

    fileInput = 'input002.txt'
    provaReadFile = readInput('input002.txt')
    provaGen = next(provaReadFile)
    provaGen2 = next(provaReadFile)
    # provaSplit = provaGen2.split(';')
    # provaSplit[0] = provaSplit[0][provaSplit[0].index(':') +2 : ]
    # provaSplitSub = provaSplit[0]
    # vediamo = stringFunction.getNumberFromString(provaSplitSub)
    testFunction = 'asldk 8988 asdòlasòlkasd  90 asdklk 00'
    testFunctionProva = stringFunction.getNumberFromString(testFunction)
    
    provaFuncDivide = divideGameBySets(provaGen)
    provaFuncDivide2 = divideSetByCubes(provaFuncDivide)
    provaFunPlayabe = checkIfPlayableGame(provaFuncDivide2, cubesOfGmes)
    
    gameNew1 = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
    gameNew1 = divideGameBySets(gameNew1)
    gameNew1 = divideSetByCubes(gameNew1)
    provaFunMin = getMinValue(gameNew1[0], cubesOfGmes)
    
    testSerious1 = analyzeGames(fileInput, cubesOfGmes, colorsList) 
    #First answer:
    #2162 DONE, CORRECT!!
    
    
    #OLD TEST FIRST PUZZLE
    # inputAoC1 = 'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green'
    # inputAoC1 = divideGameBySets(inputAoC1)
    # inputAoC1 = divideSetByCubes(inputAoC1)
    # testAoC = checkIfPlayableGame(inputAoC1, cubesOfGmes)
    
    # inputAoC2 = 'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue'
    # testAoC2 = checkIfPlayableGame(inputAoC2, cubesOfGmes)
    
    # inputAoC3 = 'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red'
    # inputAoC3 = divideGameBySets(inputAoC3)
    # inputAoC3 = divideSetByCubes(inputAoC3)
    # testAoC3 = checkIfPlayableGame(inputAoC3, cubesOfGmes)
    
    # inputAoC4 = 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red'
    # testAoC4 = checkIfPlayableGame(inputAoC4, cubesOfGmes)
    
    # inputAoC5 = 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'
    # testAoC5 = checkIfPlayableGame(inputAoC5, cubesOfGmes)
    

    