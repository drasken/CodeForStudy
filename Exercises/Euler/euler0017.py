#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 23:56:55 2024

@author: drasken
"""

map_first_ten = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}
map_eleven_to_twenty = {11:'eleven', 12:'twelve', 13: 'thirteen', 15:'fifteen', 18:'eighteen'}

def convert_num_to_ten(num:int) -> str:
    if num in map_first_ten:
        return map_first_ten[num]
    else:
        return

def convert_num_to_twenty(num:int)-> str:
    if num in map_eleven_to_twenty:
        return map_eleven_to_twenty[num]
    else:
        digit = num % 10
        s = map_first_ten[digit] + 'teen'
        return s

map_20_to_100 = {20:'twenty', 30:'thirty', 40:'fourty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

def convert_num_to_99(num:int)->str:
    if num in map_20_to_100:
        return map_20_to_100[num]
    else:
        unit = num % 10
        dec = num - unit
        s = map_20_to_100[dec] + map_first_ten[unit]
        return s
    
    

list_first_nums = [x for x in range(1,6)]

test = list(map(convert_num_to_ten, list_first_nums))
test = sum([len(x) for x in test])
