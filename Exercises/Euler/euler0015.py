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


    
    
    



