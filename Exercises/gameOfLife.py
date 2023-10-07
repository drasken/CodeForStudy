#Game of Life 

"""
The cell then updates its own liveness according to 4 rules:

    Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
    Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
    Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

"""

import random

#firts milestone

def deadState (width, height):
    line = [0 for i in range(width)]
    output = [line for j in range(height)]

    return output

#IN PROGRESS
def randomState(board):
    for i in range():
        for j in range(len(i)):
            board[i][j] = random.randint(0,1)


board = deadState(10,10)
randomState(board)

print(board)
