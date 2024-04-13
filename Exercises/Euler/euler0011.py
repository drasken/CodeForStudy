#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:45:18 2024

@author: drasken
"""

import util

#transform from str to int
def transform_data(list_of_values:list[str])->list[list]:
    
    matrix = []

    for row in list_of_values:
        new_row = row.split()
        new_row = list(map(lambda x: int(x), new_row))
        matrix.append(new_row)
    
    return matrix

def check_horizontally(matrix:list[list], step:int) -> int:
    
    max_found = 0
    
    for row_index, row in enumerate(matrix):
        for index, num in enumerate(row):
            if (index + step) > len(row):
                break
            else:
                temp_sum = util.prod_mine(row[index: index + step])
                max_found = max(max_found, temp_sum)

                    
    return max_found

def check_vertically(matrix:list[list], step: int) -> int:
    
    max_found = 0
    
    for row_index, row in enumerate(matrix):
        if (row_index + step) > len(matrix):
            break
        for index, num in enumerate(row):
           temp_sum = [matrix[row_index][index]]
           count = 1
           while count < step:
               temp_sum.append(matrix[row_index + count][index])
               count += 1
           temp_sum = util.prod_mine(temp_sum)
           max_found = max(max_found, temp_sum)

           
    return max_found

def check_diagonally(matrix:list[list], step:int) -> int:
    
    max_found = 0
    
    for row_index, row in enumerate(matrix):
        if (row_index + step) > len(matrix):
            break
        for index, num in enumerate(row):
            if (index + step) > len(row):
                break
            count = 1
            temp_sum = [matrix[row_index][index]]
            while count < step:
                temp_sum.append(matrix[row_index + count][index + count])
                count += 1
            temp_sum = util.prod_mine(temp_sum)
            max_found = max(max_found, temp_sum)
    
    return max_found
    pass

def check_diagonally_inverse(matrix: list[list], step:int) -> int:
    
    mirror_matrix = [row[::-1] for row in matrix]
    
    res = check_diagonally(mirror_matrix, step)
    
    return res
            

def find_max (matrix:list[list], step:int) -> int:
    
    pass

    
    hor_value, vert_value, diag_value, diag_mirror = check_horizontally(matrix, step), check_vertically(matrix, step), check_diagonally(matrix, step), check_diagonally_inverse(matrix, step)
    
    max_value = max(hor_value, vert_value, diag_value, diag_mirror)
    
    return max_value


if __name__ == '__main__':
    testFile = transform_data(util.read_from_file('euler0011_input.txt'))
    
    test_hor = check_horizontally(testFile, 4)

    test_vert = check_vertically(testFile, 4)

    test_diag = check_diagonally(testFile, 4)

    
    test_diag_mirr = check_diagonally_inverse(testFile, 4)

    res = find_max(testFile, 4)
    