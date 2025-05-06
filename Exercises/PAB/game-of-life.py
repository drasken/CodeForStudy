"""
Trying again do it using Python
"""

import random

# First Milestone


def dead_state(height: int, width: int) -> list[list[int]]:
    output = [[0 for i in range(width + 2)] for j in range(height + 2)]

    return output


def random_state(board: list, probability: float = 0.5) -> None:
    """
    Representing a "world" for CGOL game as a matrix of int
    This is the code: 0 = dead, 1 = alive, 2 = padding
    the parameters are the world's dimensions to render, without the padding
    """

    # use eumerate to cycle on all board elements

    height, width = len(board), len(board[0])

    for index_row, row in enumerate(board):
        for index_el, element in enumerate(row):
            if index_row == 0 or index_row == height - 1 or index_el == 0 or index_el == width - 1:
                board[index_row][index_el] = 2
            else:
                rand = random.random()
                if rand >= probability:
                    board[index_row][index_el] = 1  # else is already 0


# Done

# Second Milestone


def render(board: list[list]):

    for i_row, row in enumerate(board):
        for i_el, el in enumerate(row):
            if el == 2:
                print("#", end="")
            elif el == 1:
                print("X", end="")
            else:
                print(" ", end="")
        print("\n")


# Done
# Third Milestone

"""
Any live cell with 0 or 1 live neighbors becomes dead, because of underpopulation
Any live cell with 2 or 3 live neighbors stays alive, because its neighborhood is just right
Any live cell with more than 3 live neighbors becomes dead, because of overpopulation
Any dead cell with exactly 3 live neighbors becomes alive, by reproduction

Algo: make a new board, check old board neighbors
 than set cells on the new board accordingly
 the new board becames the new "world" to render
"""


def count_neighbors(board: list[list], y_pos: int, x_pos: int) -> int:
    """
    Use this function to calculate next state of a cell in a board
    Return 1 if alive else 0 if dead 
    """

    cell_state: int = board[y_pos][x_pos]  # must be 0 or 1
    assert cell_state >= 0 and cell_state <= 1
    
    new_state: int = 0

    count_neigh : int = 0

    for row in board[y_pos - 1: y_pos + 2]:
        for el in row[x_pos - 1: x_pos + 2]:
            if el != 2:
                count_neigh += el
    count_neigh -= cell_state

    assert count_neigh >= 0 and count_neigh <= 8

    if cell_state == 0 and count_neigh == 3:
        new_state = 1
        return new_state

    elif cell_state == 1:
        if count_neigh == 2 or count_neigh == 3:
            new_state = 1
            return new_state
    else:
        new_state = 0
        return new_state

# Tests passed

def next_board_state(board: list[list]) -> list[list]:
    """
    Given in input a board return in output a new board state
    First create a new board
    Calculate next state for each cell in the old board
    update the new board with new cell state
    return the new board
    """
    pass
    
    

def main(h: int, w: int):

    my_board = dead_state(h, w)
    random_state(my_board)

    render(my_board)


if __name__ == '__main__':

    test = main(15, 30)

    # # test count neigh
    # test_matrix = [[2,2,2,2], [2,0,1,0], [2,1,1,0],[2,0,1,0],[2,0,1,0]]
    # test_count1 = count_neighbors(test_matrix, 1, 1)  # expected 1
    # print(test_count1)
    # test_count2 = count_neighbors(test_matrix, 2, 2)  # expected 1
    # print(test_count2)
    # test_count3 = count_neighbors(test_matrix, 3, 1)  # expected 0
    # print(test_count3)

