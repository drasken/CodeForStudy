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
    testMul = util.check_horizontally(testFile2, 5, 5, 4)
    

