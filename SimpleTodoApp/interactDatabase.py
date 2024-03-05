#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:31:38 2024

@author: drasken
"""
#Functions to interact with the database, choice: CSV

import csv
import Task

def checkForDatabase(fileName: str, path: str ='.'):
    
    try:
        with open(fileName, mode='r') as dataB:
            return True
    except OSError:
        print("Can't Open this file, maybe wrong name?.")
        return
    except:
        print("Error, DB not opened.")
        return
    
    
def createDatabase (fileName: str):
    with open(fileName, mode='w'):
        pass #the file is created
        
def appendTaskToBatabase(fileName:str, task: Task):
    with open(fileName, mode='a') as dataB:
        dataB.write(task.toCsv())
        