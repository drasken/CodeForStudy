#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:01:19 2024

@author: drasken
"""
"""
Trying doing Dynamoc programming
"""

side_len = 21

my_matrix = [[0 for x in range(side_len)] for y in range(side_len)]

print(my_matrix)

def find_paths(matr):
    for index, line in enumerate(matr):
        for index_el, el in enumerate(line):
            if index == 0 or index_el == 0:
                matr[index][index_el] = 1
            else:
                matr[index][index_el] = line[index_el - 1] + matr[index - 1][index_el]
                #print(matr[index][index_el])
    return matr[-1][-1]

find_paths(my_matrix)

#print(my_matrix)

#first test = 35345263800 --> Wrong
#2nd test = 137846528820 --> OK, side too short by 1

# from collections import namedtuple
# import copy


# class Node:
    
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
    
#     def __str__(self):
#         string_children = " "
        
#         if self.left != None:
#             string_children += str(self.left.value) + " " 
#         if self.right != None:
#             string_children += str(self.right.value)
        
#         return f"node value: {self.value}. Children values:{string_children}"



# class BinaryTree:
    
#     def __init__(self, root:Node, limit:tuple):
#         self.root = root
#         self.count = 0
#         self.limit = limit
#         # self.goal = (limit, limit)
#         self.create_tree(self.root)
    
    
#     def create_tree(self, node):
        
#         if node.value[0] < self.limit:
#             left_child = Node((node.value[0] + 1, node.value[1]))
#             node.left = left_child
#             self.create_tree(node.left)
        
#         if node.value[1] < self.limit:
#             right_child = Node((node.value[0], node.value[1] + 1))
#             node.right = right_child
#             self.create_tree(node.right)
        
#         if node.value == (self.limit, self.limit):
#             self.count += 1

            
#         # if node.left == None and node.right == None:
#         #     return
        
#         # if node.right:
#         #     create_tree(node.right)
#         # if node.left:
#         #     create_tree(node.left)
            
        
    
#     def find_limit_leaves():
#         pass
    
    
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
    
    test_root = Node((0,0))
    test_tree = BinaryTree(test_root, 20)

    
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

