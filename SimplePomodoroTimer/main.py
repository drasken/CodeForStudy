#!/usr/bin/env python

""" Pomodoro main file to launch the script: it start a Pomodoro Timer in the Terminal"""

__author__ = "Drasken"
__version__ = "0.1"
__email__ = "contumax90@yahoo.it"
__status__ = "Development"

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

            elif userInput == 2:
                print("Set Timer values!")

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


