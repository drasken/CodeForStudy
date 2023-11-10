#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 23:11:05 2023

@author: drasken
"""


# def collatz (number):
#     try:
#         if number <= 0:
#             raise Exception
#         if isinstance(number, int):
#             step = 0
#             while number != 1:
#                 if number % 2 == 0:
#                     number /= 2
#                     step += 1
#                 else:
#                     number = number * 3 + 1
#                     step +=1
#             return step
#     except TypeError:
#         print(f"The input variable {number} is not an int")
#     except Exception:
#         print("Something went wrong")


def collatz(num):
    step = 1
    tempNum = num
    if tempNum <= 0:
        return -1
    while tempNum != 1:
        if tempNum % 2 == 0:
            tempNum /= 2
            step += 1
        else:
            tempNum = tempNum * 3 + 1
            step += 1
    return step

result = 0
tempStep = 0

listNum = [x for x in range(1000000)]

for i in listNum:
    tempResult = collatz(i)
    if tempResult > tempStep:
        tempStep = tempResult
        result = i

print(result)

# Solution 837799
#it works!
