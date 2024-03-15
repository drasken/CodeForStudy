#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 20:58:37 2024

@author: drasken
"""

import time
from playsound import playsound

#TODO:
#After pause function maybe refactor a generic timer function?
#Than a startRoutine function to start the study session

def setPomodoroValues() -> tuple[int]:
    pass
    #print('test') #to delete
    while True:            
        try:
            pomodoro = int(input('Set pomodoro length: '))
            pause = int(input('Set break length: '))
            
            return pomodoro,pause
        
        except ValueError:
            print('Value not correct, try again.\n')
        except KeyboardInterrupt:
            print('\n')
            break
        except Exception as e:
            print(f'Error occurred: {e}')
            break


def pomodoro(minutes: int = 30)-> None:
    """
    This function run a single pomodoro session

    Parameters
    ----------
    minutes : TYPE, int
        DESCRIPTION. Duration of the Pomodoro. The default is 30. Mus be positive.

    Returns
    -------
    str: The message to tell the Pomodoro is ended

    """
    
    countDown:int = minutes
    convertionToSeconds:int = minutes * 60
    start:float = time.time()
    prevEnding:float = start + convertionToSeconds
    
    while True:
        try:
            current_time:float = time.time() #
            current_time_h:str = time.ctime()
            print(f"Now is: {current_time_h}. Still {countDown} minutes remaining")
            countDown -= 1
            if current_time >= prevEnding:
                print('Pomodoro ended')
                #testing playing sound
                playsound('mixkit-digital-clock-digital-alarm-buzzer-992.wav')
                break
        except KeyboardInterrupt:
            print("countDown interrupted!")
            break
        except Exception as e:
            print(f"Exception occurred: {e}")
            break
        time.sleep(60)
    
    #print('Pomodoro ended')
    # return "Pomodoro Ended"


def pause(minutes: int = 5)->str:
    pass
    
    #this repeat pomodoro function, refactor(?)
    convertionToSeconds: int = minutes * 60
    start: float = time.time()
    prevEnding: float = start + convertionToSeconds
    
    while True:
        try:
            current_time: float = time.time()
            current_time_h:str = time.ctime()
            print(f'Now is {current_time_h}')
            if current_time >= prevEnding:
                print('Break ended.')
                playsound('mixkit-digital-clock-digital-alarm-buzzer-992.wav')
                break
        except KeyboardInterrupt:
            print("Break interrupted")
            break
        except Exception as e:
            print(f"Exception occurred: {e}")
            break
        time.sleep(60)
    return "Break Ended"
    
if __name__ == '__main__':
    #provaPomodoro = pomodoro(1)
    provaSet = setPomodoroValues()