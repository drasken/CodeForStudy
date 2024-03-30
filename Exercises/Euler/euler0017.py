#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 23:56:55 2024

@author: drasken
"""

map_first_ten = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}
map_eleven_to_twenty = {11:'eleven', 12:'twelve', 13: 'thirteen', 15:'fifteen', 18:'eighteen'}
map_20_to_100 = {20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}



def convert_num__one_to_ten(num:int) -> str:
    if num in map_first_ten:
        return map_first_ten[num]
    else:
        return

def convert_num__11_to_19(num:int)-> str:
    if num in map_eleven_to_twenty:
        return map_eleven_to_twenty[num]
    else:
        digit = num % 10
        s = map_first_ten[digit] + 'teen'
        return s


def convert_num_20_to_99(num:int)->str:
    if num in map_20_to_100:
        return map_20_to_100[num]
    else:
        unit = num % 10
        dec = (num // 10) * 10
        s = map_20_to_100[dec] + map_first_ten[unit]
        return s
    

def convert_num_100_to_999(num:int)->str:
    
    hund_digit = num // 100
    other_digits = num % 100
    
    if other_digits == 0:
        return map_first_ten[hund_digit] + 'hundred'
    else:
        s = map_first_ten[hund_digit] + 'hundredand'
        if other_digits <= 10:
            return s + convert_num__one_to_ten(other_digits)
        elif other_digits <= 19:
            return s + convert_num__11_to_19(other_digits)
        else:
            return s + convert_num_20_to_99(other_digits)
        
    
def convert_wrapper(num: int)->str:
    
    if num < 1 or num > 1000:
        return
    
    if num >= 1 and num <= 10:
        return convert_num__one_to_ten(num)
    elif num <= 19:
        return convert_num__11_to_19(num)
    elif num <= 99:
        return convert_num_20_to_99(num)
    elif num <= 999:
        return convert_num_100_to_999(num)
    else:
        return 'onethousand'
    

def check_function_len(word:str, num:int):
    
    word_len = len(word)
    len_function = len(convert_wrapper(num))
    assert word_len == len_function, f"erroe with {num}, you got {len_function} instead of {word_len} "

    
if __name__ == '__main__':
    
    list_first_nums = [x for x in range(1,1001)]

    test_func = list(map(convert_wrapper, list_first_nums))
   
    sol_func1 = sum([len(x) for x in test_func])
 
    print(len(convert_wrapper(115)))
    
    check_function_len('Onehundredandfifteen', 115)
    check_function_len('twohundredandnineteen', 219)
    check_function_len('fourhundredandsixtytwo', 462)
    check_function_len('twohundred', 200)
    check_function_len('onethousand', 1000)
    check_function_len('ninehundredandeightyforu', 984)
