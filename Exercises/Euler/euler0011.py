#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:45:18 2024

@author: drasken
"""

from functools import reduce
from util import read_from_file

#transform from str to int
def transform_data(list_of_values:list[str])->list[int]:
    
    matrix = []

    for row in list_of_values:
        new_row = row.split()
        new_row = list(map(lambda x: int(x), new_row))
        matrix.append(new_row)
    
    return matrix

#use this to check moltiplication horizontally
def check_horizontally(matrix: list[list], row_index: int, column_index: int, length_word: int)-> int:
    
    portion = matrix[row_index][column_index: column_index + length_word]
    
    res = reduce(lambda x,y: x * y, portion, 1)
    
    return res

def check_vertically():
    pass

if __name__ == '__main__':
    testFile = read_from_file('euler0011_input.txt')
    testFile2 = transform_data(testFile)
    testMul = check_horizontally(testFile2, 5, 5, 2)
    

