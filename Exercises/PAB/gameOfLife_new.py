#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 22:52:56 2024

@author: drasken
"""

import random
import time

#Firts milestone

def deadState (width, height):
    output = [[0 for i in range(width)] for j in range(height)]

    return output

#Done
def randomState (board, probability = 0.4):

    width = len(board)
    height = len(board[0])

    for i in range(width):
        for j in range(height):

            rand = random.random()
            if rand >= probability:
                board[i][j] = 1
            else:
                board[i][j] = 0    

    
def create_board(width, height):
    
    board = deadState(width, height)
    randomState(board)
    
    return board

#Second Milestone

def printLine(lisNum):
    line = ''
    for i in lisNum:
        if i == 1:
            line += '#'
        else:
            line += ' '
            
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

"""
    Rules:
    Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
    Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
    Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
    Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

"""

def find_neighbors(board:list, y_index:int, height:int, x_index:int, width:int) -> list:
    
    pass
    res_list = []
    
    for row in board[y_index: y_index + height]:
        for cell in row[x_index: x_index + width]:
            res_list.append(cell)
    
    return res_list

def count_neighbors(list_cells:list) -> int:
    
    pass
    count = 0
    
    for cell in list_cells:
        if cell == 1:
            count += 1
    
    return count

def dead_or_alive(neighbors, cell_state):
    
    if cell_state == 0 and neighbors == 3:
        return 1
    else:
        if neighbors <= 1:
            return 0
        elif neighbors <= 3:
            return 1
        else:
            return 0
    
    pass

def next_board_state(board):
    
    pass
    new_board = [[x for x in row] for row in board]
    
    last_y = len(board) - 1
    last_x = len(board[0]) - 1
    
    for index_row, row in enumerate(board):
        for index, cell in enumerate(row):
            if index_row == 0 and index == 0: #left upper angle
                neighbors = count_neighbors(find_neighbors(board, 0, 2, 0, 2))
                new_board[0][0] = dead_or_alive(neighbors, cell)
            elif index_row == 0 and index == last_x: #right upper angle
                neighbors = count_neighbors(find_neighbors(board, 0, 2, (last_x - 2), 2))
                new_board[0][last_x] = dead_or_alive(neighbors, cell)
            elif index_row == last_y and index == 0: #left down angle
                neighbors = count_neighbors(find_neighbors(board, (last_y - 2), 2, 0, 2))
                new_board[last_y][0] = dead_or_alive(neighbors, cell)
            elif index_row == last_y and index == last_x: #right down angle
                neighbors = count_neighbors(find_neighbors(board, (last_y - 2), 2, (last_x - 2), 2))
                new_board[last_y][last_x] = dead_or_alive(neighbors, cell)
            elif index_row == 0: #upper edge
                neighbors = count_neighbors(find_neighbors(board, 0, 2, (index - 1), 3))
                new_board[index_row][index] = dead_or_alive(neighbors, cell)
            elif index_row == last_y: #bottom edge
                neighbors = count_neighbors(find_neighbors(board, (last_y - 1), 2, (index - 1), 3))
                new_board[index_row][index] = dead_or_alive(neighbors, cell)
            elif index == 0: #left edge
                neighbors = count_neighbors(find_neighbors(board, (index_row - 1), 3, index, 2))
                new_board[index_row][index] = dead_or_alive(neighbors, cell)
            elif index == last_x: #right edge
                neighbors = count_neighbors(find_neighbors(board, (index_row - 1), 3, (index - 1), 2))
                new_board[index_row][index] = dead_or_alive(neighbors, cell)
            else:
                neighbors = count_neighbors(find_neighbors(board, (index_row - 1), 3, (index - 1), 3))
                new_board[index_row][index] = dead_or_alive(neighbors, cell)
              
    return new_board


def main(height, width):
    
    board = create_board(height, width)
    
    while True:
        render(board)
        
        board = next_board_state(board)
        
        time.sleep(1)
        
    
    
if __name__ == '__main__':
    
    main(20, 20)
    
    # test_board = create_board(10, 10)
    # render(test_board)
    
    # prova_next = next_board_state(test_board)
    # render(prova_next)
    
    