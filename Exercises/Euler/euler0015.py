#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:01:19 2024

@author: drasken
"""

from collections import namedtuple
import copy


Coordinate = namedtuple('Coordinate', ["row", "column"])

dimension = 20


#creating a matrix representing the problem 

grid = [[(z, y) for y in range(dimension)] for z in range(dimension)]

def add_step(path_list:list[tuple], limit:int) -> list[tuple]:
    #controlling limiti i'll do it in the  outer function
    
    pass
    last_step = path_list[-1]
    #check = limit - 1
    
    res = []
    
    if last_step[0] < limit:
        temp_path = copy.copy(path_list)
        temp_path.append((last_step[0] + 1, last_step[1]))
        res.append(temp_path)
    
    if last_step[1] < limit:
        temp_path2 = copy.copy(path_list)
        temp_path2.append((last_step[0], last_step[1] + 1))
        res.append(temp_path2)
        
    return res

def calculate_paths(starting_point: list[list[tuple]], limit:int) -> list[list[tuple]]:
    pass
    #start adding from the starting point
    
    res = []
    
    for path in starting_point:
        to_add = add_step(path, limit)
        res.extend(to_add)
    
    return res

def check_if_ending(list_paths:list, limit:int) -> bool:
    
    #check if can continue iteration
    
    check = True
    
    for el in list_paths:
        if el[-1][0] < limit or el[-1][1] < limit:
            return check
    
    return False
        
    
    
def calc_all_paths(start:list, limit:int) -> int:

    temp_pahts = copy.deepcopy(start)
    
    new_temp_pahts = calculate_paths(temp_pahts, limit)
    
    #function check if stop iteration
    
    
    
      

if __name__ == '__main__':
    #test function add_Step
    path_1 = [(0,1)]
    res_1 = add_step(path_1, 4) #expected [[(0, 1), (1, 1)], [(0, 1), (0, 2)]]
    print(res_1) #ok
    
    path_2 = [(2,3), (2,4),(2,5), (3,5), (3,6)]
    res_2 = add_step(path_2, 10)   
    #expected -> [[(2,3), (2,4),(2,5), (3,5), (3,6), (4,6)], [(2,3), (2,4),(2,5), (3,5), (3,6), (3,7)]]
    print(res_2)
    #testing for limit
    path_3 = [(2,3), (2,4),(2,5), (3,5), (3,6)]
    res_3A = add_step(path_2, 2) #expectiong []
    print(res_3A)
    res_3B = add_step(path_2, 4)   #expectiong [[(2,3), (2,4),(2,5), (3,5), (3,6), (4,6)]
    print(res_3B)
    #ok!

    #testing calculate function
    calculate_1 = [[(0,0)]]
    calc_1 = calculate_paths(calculate_1, 20)
    print(calc_1)
    
    #test check function
    check_1 = [[(2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (4, 6)], [(2, 3), (2, 4), (2, 5), (3, 5), (3, 6), (3, 7)]]
    res_check = check_if_ending(check_1, 20)
    res_checkB = check_if_ending(check_1, 3)
    



