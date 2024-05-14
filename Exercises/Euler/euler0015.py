#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:01:19 2024

@author: drasken
"""

from collections import namedtuple
import copy


class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __str__(self):
        string_children = " "
        
        if self.left != None:
            string_children += str(self.left.value) + " " 
        if self.right != None:
            string_children += str(self.right.value)
        
        return f"node value: {self.value}. Children values:{string_children}"


class BinaryTree:
    
    def __init__(self, root:Node, limit:tuple):
        self.root = root
        self.count = 0
        self.limit = limit
        
    def find_limit_leaves():
        pass
    
    
# =============================================================================
# def add_path(list_path:list[tuple], limit:int) -> list[tuple]:
#     
#     last_step = list_path[-1]
#     res_paths = []
#     
#     if last_step[0] < limit:
#         path_to_add = copy.deepcopy(list_path)
#         path_to_add.append((last_step[0] + 1, last_step[1]))
#         res_paths.append(path_to_add)
#     
#     if last_step[1] < limit:
#         path_to_add = copy.deepcopy(list_path)
#         path_to_add.append((last_step[0], last_step[1] + 1))
#         res_paths.append(path_to_add)
# 
#     return res_paths
# 
# def calculate_path(list_path: list[list[tuple]], limit:int) -> int:
#     
#     total_paths = copy.deepcopy(list_path)
#     
#     while True:
#         temp_paths = []
#         for li in total_paths:
#             pass
# =============================================================================

if __name__ == '__main__':
    pass

    test_node = Node((0,0))
    test_left_child = Node((1,0))
    test_right_chilfd = Node((0,1))
    test_node.right, test_node.left = test_right_chilfd, test_left_child
    print(test_node)
    
# =============================================================================
#     #test function add_path()
#     test = [(2,3), (2,4),(2,5), (3,5), (3,6)]
#     test2 = [(4,4), (5,4),(5,5), (6,5), (7,5), (8,5), (9,5), (9,6)]
#     res_test = add_path(test, 8)
#     res_test2 = add_path(test2, 8)
#     res_test_formatted = []
#     res_test_formatted.extend(res_test2)
#     res_test_formatted.extend(res_test)
# 
#     print(res_test)    
# 
# =============================================================================

