#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 00:01:28 2024

@author: drasken
"""

import util

names = util.read_from_file('euler_0022_names_input.txt')

#process data to use them

names = names[0].split(',')
names = [x.strip('\"') for x in names]
names.sort() #now I have just the names

#assign value to each letter
letters_dict = {chr(x): x - 64 for x in range(65, 91)}

def calculate_name_value(name:str)->int:
    
    letters = list(name)
    
    letters = [letters_dict[x] for x in letters]
    
    return sum(letters)

# test = calculate_name_value('COLIN') #OK

total = 0

for index, name in enumerate(names):
    total += (index + 1) * calculate_name_value(name)
    
print(total) #solution --> 871198282 OK!!
