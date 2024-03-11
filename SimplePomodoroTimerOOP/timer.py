#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 16:13:28 2024

@author: drasken
"""

"""The module for the Time class, his dubclass anf the functions related"""

import time

class Timer:
    """
    The class used to represent object Timer in the main function for the pomodoro script.
    """

    def __init__(self):
        self.start = time.time(), time.ctime()
    
    def __str__(self):
        return f'The timer started at {self.start[1]}'
    
    def ringBellOnEnding(self): #to implement, ring the bell when the countdown ends
        pass
    
class Routine:
    "This class start the routine when starting a Pomodoro session"
    
    def __init__(self, tupleTimer = (5)):
        self.tupleTimer = [ Timer() for x in range(tupleTimer)]
        
    def __str__(self):
        return "\n".join([timer.__str__() for timer in self.tupleTimer])
        
    
        
if __name__ == '__main__':
    testTimer = Timer()
    testRoutine = Routine()
    
    print(testRoutine)



