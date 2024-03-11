#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:58:37 2024

@author: drasken
"""

import time

def pomodoro(minutes: int = 30)->str:
    """

    Parameters
    ----------
    minutes : TYPE, int
        DESCRIPTION. Duration of the Pomodoro. The default is 30.

    Returns
    -------
    str

    """
    
    start: float = time.time()
    convertionToSeconds: int = minutes * 60
    prevEnding: float = start + convertionToSeconds
    
    
    
    return start
    
if __name__ == '__main__':
    provaPomodoro = pomodoro()