#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 15:13:28 2024

@author: drasken
"""

#__status__ = "Development"

"""
TODO:
    - Add a schedule function to call pomodoro and pause function
    - Generalize a timer function and than differentiate in pomororo and pause(?)
    - Let's see if TUI can be improved'
    - Maybe expose/translate it as webapp(?)
"""
    

import pomodoro

def main():
    while True:
        messageToPrint = """Welcome to Pomodoro Timer, select an option:
        1 -> Start new Timer
        2 -> Set Timer time values
        3 -> Quit the script
        """
        print(messageToPrint)
        
        try:
            userInput = int(input("Choose your option: "))
        

            if userInput == 1:
                print("Let's start a new timer!")
                pomodoro.pomodoro()
                pomodoro.pause()
                pomodoro.pomodoro()
                pomodoro.pause(15)
                break

            elif userInput == 2:
                print("Set Timer values!")
                pomodoroMod, pauseMod = pomodoro.setPomodoroValues()
                pomodoro.pomodoro(pomodoroMod)
                pomodoro.pomodoro(pauseMod)
                #break

            elif userInput == 3:
                print("See you again!")
                break

        except ValueError:
            print("Invalid input, try again :) \n")
            
        except KeyboardInterrupt:
            print("\nYou terminated the execution by Keyboard, see you again :) ")
            break
    

        
    

if __name__ == "__main__":
    main()


