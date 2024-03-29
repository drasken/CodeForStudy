#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:45:18 2024

@author: drasken
"""

import util

#transform from str to int
def transform_data(list_of_values:list[str])->list[int]:
    
    matrix = []

    for row in list_of_values:
        new_row = row.split()
        new_row = list(map(lambda x: int(x), new_row))
        matrix.append(new_row)
    
    return matrix


if __name__ == '__main__':
    testFile = util.read_from_file('euler0011_input.txt')
    testFile2 = transform_data(testFile)
    # testMul = util.check_horizontally(testFile2, 5, 5, 4)
    
    max_temp = 0
    
    sol = list()
    
    hor_limit = (len(testFile2) - 4)
    for row_index, row in enumerate(testFile2):
        for col_index, el in enumerate(row[:hor_limit]): 
            if el == 0:
                continue
            else:
                hor = util.check_horizontally(testFile2, row_index, col_index, 4)
                if hor[0] > max_temp:
                    max_temp = hor[0]
                    sol = hor[1]
    
    #NOT WORKING!!!
    ver_limit = (len(testFile2) - 4)
    for row_index, row in enumerate(testFile2[:ver_limit]):
        for col_index, el in enumerate(row): 
            if el == 0:
                continue
            else:
                ver = util.check_vertically(testFile2, row_index, col_index, 4)
                if ver[0] > max_temp:
                    max_temp = ver[0]
                    sol = ver[1]
                    
            
    diag_limit = (len(testFile2) - 4)
    for row_index, row in enumerate(testFile2[:diag_limit]):
        for col_index, el in enumerate(row[:diag_limit]): 
            if el == 0:
                continue
            else:
                ver = util.check_vertically(testFile2, row_index, col_index, 4)
                if ver[0] > max_temp:
                    max_temp = ver[0]
                    sol = ver[1]
                    
    

