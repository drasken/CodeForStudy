"""
This will be my main funciton to sudoku solver
To see further documentation, see notes.org
"""


import random
import pprint  # Useful for debugging
import numpy as np


# GLOBAL VARIABLES HERE ---------------
POPULATE_PARAM_EASY: float = 0.80
POPULATE_PARAM_MEDIUM: float = 0.65
POPULATE_PARAM_HARD: float = 0.50
POPULATE_PARAM_VERY_HARD: float = 0.3


def init_empty_table() -> list[list]:
    """
    Make an initial empty sudoku table.
    The dimension es the classic 9x9 sudoku
    """
    my_table: list[list] = [[0 for x in range(9)] for y in range(9)]

    return my_table


def randomize_table(table: list[list]) -> None:
    """
    Modify a given table in place
    """
    for row_index, row in enumerate(table):
        for index, elemenet in enumerate(row):
            if random.random() < POPULATE_PARAM_EASY:  # CHANGE HARD CODED PARAM
                table[row_index][index] = random.randint(1,9)
            else:
                table[row_index][index] = 0  # Be sure to set as empty cell
    return


def get_block(y_index: int, x_index: int) -> list:
    pass


def main():
    """
    Main function, my simple app entry point
    """
    my_table: list[list] = init_empty_table()
    randomize_table(my_table)
    my_transpose = np.transpose(my_table)
    
    return my_table


test = main()
