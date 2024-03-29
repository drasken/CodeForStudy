#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 22:52:38 2024

@author: drasken
"""

"""
Util for solving Euler Problem
"""
import math 
from functools import reduce


def read_from_file(filename:str)->list:
    """
    Simple util function to read input fil a string for the Project Euler problems

    Parameters
    ----------
    filename : str
        the file_path name.

    Returns
    -------
    list
        the lines of the file returnd as string in a list.

    """
    
    with open(filename, mode='r') as f:
        
        res = f.readlines()
        
        return res
    

def findDiv2(num: int) -> int:
    """
    Find all the divisor for the number  in input [1, num] included

    Parameters
    ----------
    num : int
        The number of wich to find divisor.

    Returns
    -------
    int
        The number of divisors found.

    """
    
    count = 0

    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if num / i == i:
                count += 1
            else:
                count += 2
    
    return count
    

def check_if_evely_divisible(list_of_divisors: list, num_to_check: int)-> bool:
    """
    Used for checking if the numbers in the provided list are evenly divisible (?)

    Parameters
    ----------
    list_of_divisors : list
        DESCRIPTION.
    num_to_check : int
        DESCRIPTION.

    Returns
    -------
    bool
        DESCRIPTION.

    """
    for num in list_of_divisors:
        if num_to_check % num != 0:
            return False
    
    return True

#used for problem 003
def sieve_E2(limit: int)-> list:
    """
    Implementation of Sieve of Eratostene to find prime numbers within limit number given in input


    Parameters
    ----------
    limit : int
        The number limit within we want to find prime numbers, limit included.

    Returns
    -------
    list
        List of integers from 2 to limit

    """
    
    counter = 2
    
    list_nums = [x for x in range(2,limit +1) if x == 2 or x %2 != 0]
    
    while counter < (limit ** 0.5):
        if counter not in list_nums:
            counter += 1
            continue
        else:
            list_nums = [x for x in list_nums if x == counter or x % counter != 0]
            counter += 1
    
    return list_nums


#Utils for Matrix -------------------------------------------------------------

#use this to check moltiplication horizontally
def check_horizontally(matrix: list[list], row_index: int, column_index: int, length_word: int)-> int:
    
    portion = matrix[row_index][column_index: column_index + length_word]
    
    res = reduce(lambda x,y: x * y, portion, 1)
    
    return res,portion

#check vertical in matrix
def check_vertically(matrix:list[list], row_index:int, column_index:int, len_word:int)-> int:
    pass
    
    
    section = [[matrix[x][column_index] for x in li] for li in matrix[row_index:row_index + len_word]]
    
    res = reduce(lambda x,y: x * y, section, 1)
    
    return res, section

def check_diag(matrix:list[list], row_index:int, column_index:int, len_word:int)-> int:
    
    section = list()
    
    for row_num, row in enumerate(matrix[row_index: len_word]):
        for col_num, num in enumerate(row[column_index: len_word]):
            if row_num == col_num:
                section.append(num)
                
    res = reduce(lambda x,y: x * y, section, 1)

    return res

if __name__ == '__main__':
    pass
    # test = [x for x in range (2,20)]
    
    # test2 = changeValue(test, 2)
    # test3 = changeValue(test, 3)
    
    testSieve = sieve_E2(20)
    first_ten = [x for x in  range(1,11)]
    
    testDiv = check_if_evely_divisible(first_ten, 2520) #exp True
    testDiv = check_if_evely_divisible(first_ten, 2521) #exp False