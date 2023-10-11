#Game of Life 

"""
The cell then updates its own liveness according to 4 rules:

    Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
    Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
    Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

"""

import random

#Firts milestone

def deadState (width, height):
    output = [[0 for i in range(width)] for j in range(height)]

    return output

#Done
def randomState (board, probability = 0.5):

    width = len(board)
    height = len(board[0])

    for i in range(width):
        for j in range(height):

            rand = random.random()
            if rand >= probability:
                board[i][j] = 1
            else:
                board[i][j] = 0    

    

#Second Milestone

def printLine(lisNum):
    line = ''
    for i in lisNum:
        if i == 1:
            line += '#'
        elif i == 0:
            line += ' '
        else:
            continue     
    return line       

#DONE

def render(state):
    width = len(state[0])
    upBottomLines = '-' * width
    newState = ''
    for i in state:
        newPrintedLine = '|' + printLine(i) + '|\n'
        newState += newPrintedLine
    print(' ' + upBottomLines + ' ')
    print(newState)
    print(' ' + upBottomLines + ' ')

#DONE

#Third Milestone

#probably need to implement a checkIfAlive function
def next_board_state(state):
    pass


def checkCellState(cell, nearCellsCount): #return the int nu tu put in the tab
    """
    Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
    Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
    Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

    """
    if cell == 0:
        if nearCellsCount == 3:
            return 1
        else:
            return 0
    elif cell == 1:
        if nearCellsCount == 0 or nearCellsCount == 1:
            pass #da finire
    



board = deadState(10,10)
board[2][4] = 6
board[2][6] = 6
board[2][8] = 6
print(board)

bo = board [0] is board [2]
print(bo)
randomState(board)
test = [x for x in range (10)]

print (board)

render(board)
