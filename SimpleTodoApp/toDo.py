#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:30:37 2024

@author: drasken
"""
#Main file in which ro run the main() function

import interactDatabase
from Task import Task

#Global Variables

def main():
    
    databaseName = 'tasks.csv'
    
    #create the badabase anyway in cwd
    if not interactDatabase.checkForDatabase(databaseName):
        interactDatabase.createDatabase(databaseName)

    while True:
        try:
        
            print("""What do you whant to do?\n 
                  1: Add a task\n
                  2: Read pending tasks\n
                  3: Quit the program\n""")
            
            choice = ('Make your choice: ')
            
            name = input('Add a task name or quit:')
            
            if choice == 1:
                taskToAdd = Task.createNewTask() 
                interactDatabase.appendTaskToBatabase(databaseName, taskToAdd)
            
            
        except Exception:
            print('\n Shutting down the prgram. So long. :)')
            break
        


#First try to find the database, SQLite probably

if __name__ == '__main__':
    main()
    taskProva = Task('Partita', 'giochiamo a calcio')
    interactDatabase.appendTaskToBatabase('tasks.csv', taskProva)
    taskProva2 = Task('Pulizie', 'lava la terrazza')
    interactDatabase.appendTaskToBatabase('tasks.csv', taskProva)
    readList = interactDatabase.readAllTasks('tasks.csv')
    
                                          
                                          