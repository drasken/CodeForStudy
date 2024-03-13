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
    
    convertionToSeconds: int = minutes * 60
    start: float = time.time()
    prevEnding: float = start + convertionToSeconds
    
    while True:
        try:
            current_time: float = time.time()
            current_time_h = time.ctime()
            print(f"Now is: {current_time_h}")
            if current_time >= prevEnding:
                break
        except KeyboardInterrupt:
            print("countDown interrupted!")
            break
        time.sleep(5)
    
    
    return "Pomodoro Ended"
    
if __name__ == '__main__':
    provaPomodoro = pomodoro(1)