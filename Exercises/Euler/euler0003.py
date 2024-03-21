#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 17:18:09 2024

@author: drasken
"""

from util import sieve_E


if __name__ == '__main__':
    
    number_to_factorize = 600851475143
    limit_for_primes = number_to_factorize ** 0.5 #square root
    ex003 = sieve_E(limit_for_primes)
    for num in ex003[::-1]:
        if number_to_factorize % num == 0: #found biggest prime factor
            print(num)
            break
    
    #solved: 6857