#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:30:37 2024

@author: drasken
"""
#Main file in which ro run the main() function

import interactDatabase

#Global Variables
databaseName = 'tasks.csv'

def main():
    interactDatabase.readDatabase(databaseName)


#First try to find the database, SQLite probably

if __name__ == '__main__':
    main()