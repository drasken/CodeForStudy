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
databaseName = 'tasks.csv'

def main():
    if not interactDatabase.checkForDatabase(databaseName):
        interactDatabase.createDatabase(databaseName)


#First try to find the database, SQLite probably

if __name__ == '__main__':
    main()
    taskProva = Task('Partita', 'giochiamo a calcio')
    interactDatabase.appendTaskToBatabase('tasks.csv', taskProva)