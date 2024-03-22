#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 22:52:38 2024

@author: drasken
"""

"""
Util for solving Euler Problem
"""

def read_from_file(filename:str)->list:
    
    with open(filename, mode='r') as f:
        
        res = f.readlines()
        
        return res
    
    

def check_if_evely_divisible(list_of_divisors: list, num_to_check: int)-> bool:
    
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

# def sieve_E(limit: int)-> list:
#     """
#     Implementation of Sieve of Eratostene to find prime numbers within limit number given in input

#     Parameters
#     ----------
#     limit : int
#         The number limit within we want to find prime numbers, limit included.

#     Returns
#     -------
#     list
#         List of integers from 1 included to limit

#     """
    
#     list_nums = [True for x in range(limit + 1)]
    
#     for index, el in enumerate(list_nums):
#         if index == 0 or index == 1:
#             list_nums[index] = False
#         elif el == False:
#             continue
#         else:
#             for new_index, mul in enumerate(list_nums):
#                 if new_index > index and new_index % index == 0:
#                     list_nums[new_index] = False
    
#     list_res = [1] #this supposing we wnat to include 1, else empty list
    
#     for position, bo in enumerate(list_nums):
#         if bo == True:
#             list_res.append(position)
            
#     return list_res

if __name__ == '__main__':
    pass
    # test = [x for x in range (2,20)]
    
    # test2 = changeValue(test, 2)
    # test3 = changeValue(test, 3)
    
    testSieve = sieve_E2(20)
    first_ten = [x for x in  range(1,11)]
    testDiv = chek_if_evely_divisible(first_ten, 2520) #exp True
    testDiv = chek_if_evely_divisible(first_ten, 2521) #exp False