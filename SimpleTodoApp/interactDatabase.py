#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:31:38 2024

@author: drasken
"""
#Functions to interact with the database, choice: CSV

import csv

def readDatabase(fileName: str, path: str ='.'):
    
    try:
        with open(fileName, mode='r') as dataB:
            csvReader = csv.reader(dataB)
            print('ok')
    except:
        print("Missing file.")
    pass
    
    