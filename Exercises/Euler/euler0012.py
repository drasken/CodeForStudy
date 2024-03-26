#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 09:45:18 2024

@author: drasken
"""

#Project Euler Problem 0012

from util import findDiv2


# def findDiv(num: int) -> int:
#     #first version, super inefficient
    
#     res = []
    
#     for i in range(1, num + 1):
#         if num % i == 0:
#             res.append(i)
    
#     return res



def ex0012(lengthDiv: int) -> bool:
    
    index = 1
    numTr = 0
    
    while True:
        numTr += index
        index += 1
        
        if findDiv2(numTr) > lengthDiv:
            return numTr
        
        
if __name__ == '__main__':
    
    solution = ex0012(500) #Slution --> 76576500 OK!

