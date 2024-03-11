#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:13:28 2024

@author: drasken
"""

"""The module for the Time class, his dubclass anf the functions related"""

import time

class Timer:
    

    def __init__(self):
        self.start = time.time(), time.ctime()
    
    def __str__(self):
        return f'The timer started at {self.start[1]}'
        
if __name__ == '__main__':
    testTimer = Timer()



