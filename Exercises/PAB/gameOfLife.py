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


def deadState(width: int, height: int) -> list[list[int]]:
    output: list = [[0 for i in range(width)] for j in range(height)]

    return output

# Done


def randomState(board: list[list[int]], probability: float = 0.5):

    width: int = len(board)
    height: int = len(board[0])

    for i in range(width):
        for j in range(height):

            rand = random.random()
            if rand >= probability:
                board[i][j] = 1
            else:
                board[i][j] = 0


# Second Milestone

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


def render(state: list[list[int]]):
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


if __name__ == '__main__':

    board = deadState(10,10)
    render(board)
    randomState(board)
    render(board)
#   print(type(board))



# #probably need to implement a checkIfAlive function
# def next_board_state(state): #use next function for 
#     width = len(state)
#     height = len(state[0])
#     newState = deadState(width, height )
#     for i in range(width):
#         for j in range(height):
#             cell = (i, j) #tuple of index
#             #use checkCellState function
#             #checkCellState(state,cell)
#             #here the idea is tu return a 1 or 0 depending of the state
#             # with the function checkCellState            
#             newState[i][j] = checkCellState(state,cell)
#     return newState                     

# def checkCellState(board, cell): #return the int num tu put in the tab
#     """
#     Check for dead or alive neighbors.
#     Cell is a List of index for the position of the Cell in the Grid.
#     Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
#     Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
#     Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
#     Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

#     """
#     width = len(board[0])
#     height = len(board)
#     aliveCells = 0
#     #Pseudocodice per me, da cancellare
#     # ad ogni check se tovo un 1 aggiungi += 1 a aliveCells
#     #if cell[0] == 0: #first row
#     if cell[0] == 0:#first row
        
#     #  if cell[1] == 0 or == len(stat[0]):
#         if cell[1] == 0: #check angle up left
#             aliveCells += board[0][2].count(1)
#             aliveCells += board[1][:2]
#         elif cell[1] == width -1: #check angle up right
#             aliveCells += board[0][width -1].count(1)
#             aliveCells += board[1][width -2:].count(1)
#         #    chech for angle
#         else: #the board is on top row not an angle
#             pass
#     #elif cell[1] == 0 or come sopra:
#     #  sono in un borso laterale
#     #elif: #come per la prima file ma invertita
#     #  check solo per 5 posizioni
#     #elif:
#     # check per le posizioni normali, 8 vicini
#     #here start counting

#     #if DA IMPLEMENTARE 
    

    
#     if aliveCell == 0:
#         if nearCellsCount == 3:
#             return 1
#         else:
#             return 0
#     elif aliveCell == 1:
#         if nearCellsCount == 0 or nearCellsCount == 1:
#             return 0
#         if nearCellsCount == 2 or nearCellsCount == 3:
#             return 1
#         if nearCellsCount > 3:
#             return 0
#     # eventually add error handling etc.    

# def calcNeighbor(tab):
#     pass
    
    
    



# board = deadState(10,10)
# board[2][4] = 6
# board[2][6] = 6
# board[2][8] = 6
# print(board)

# bo = board [0] is board [2]
# print(bo)
# randomState(board)
# test = [x for x in range (10)]

# print(board)

# render(board)

# test3 = next_board_state(board)
# print(test3)
