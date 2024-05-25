#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 23:13:08 2024

@author: drasken
"""

"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""

import math

"""
Give number position to find:
    starting from all ciphers(10) factorial and fraction
    divide for nunmber of ciphers
    multiply if <= limit
        if == limit return 
        if >= limit
            continue the same algorithm for cipher -1 until limit found
    
"""

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
# =============================================================================
# 
# sorted_numbers = sorted(numbers)
# 
# print(sorted_numbers)
# 
# first_fract = math.factorial(10) / 10
# 
# test = first_fract * 3
# print(first_fract)
# print(test)
# 
# second_fract = math.factorial(9) / 9
# print(second_fract)
# 
# 
# 
# test2 = first_fract * 2 + (second_fract * 6)
# print(test2)
# 
# 
# =============================================================================

def find_position(ciphers: int, limit:int, start:int = 0, solution:list[int] = []) -> list[int]:
    
    fraction:int = math.factorial(ciphers) / ciphers
    
    for i in range(1, ciphers + 1):
        if fraction * i + start == limit:
            solution.append(i)
            break
        elif fraction * i + start > limit:
            solution.append(i-1)
            break
        
    return solution
    
if __name__ == '__main__':
    test = find_position(10, 1000000)
    print(test)
    
