#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:01:19 2024

@author: drasken
"""

from collections import namedtuple
import copy

def add_path(list_path:list[tuple], limit:int) -> list[tuple]:
    
    last_step = list_path[-1]
    res_paths = []
    
    if last_step[0] < limit:
        path_to_add = copy.deepcopy(list_path)
        path_to_add.append((last_step[0] + 1, last_step[1]))
        res_paths.append(path_to_add)
    
    if last_step[1] < limit:
        path_to_add = copy.deepcopy(list_path)
        path_to_add.append((last_step[0], last_step[1] + 1))
        res_paths.append(path_to_add)

    return res_paths

if __name__ == '__main__':
    pass
    
    #test function add_path()
    test = [(2,3), (2,4),(2,5), (3,5), (3,6)]
    test2 = [(4,4), (5,4),(5,5), (6,5), (7,5), (8,5), (9,5), (9,6)]
    res_test = add_path(test, 8)
    res_test2 = add_path(test2, 8)
    res_test_formatted = []
    res_test_formatted.extend(res_test2)
    res_test_formatted.extend(res_test)

    print(res_test)    


