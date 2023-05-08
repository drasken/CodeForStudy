#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 23:11:05 2023

@author: drasken
"""


def collatz (number):
    try:
        if number <= 0:
            raise Exception
        if isinstance(number, int):
            step = 0
            while number != 1:
                if number % 2 == 0:
                    number /= 2
                    step += 1
                else:
                    number = number * 3 + 1
                    step +=1
            return step
    except TypeError:
        print(f"The input variable {number} is not an int")
    except Exception:
        print("Something went wrong")
    
        
    