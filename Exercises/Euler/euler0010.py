"""The sum of the primes below 10  is 2+3+5+7 = 17.

Find the sum of all the primes below two million.

"""

from util import sieve_E2
    
if __name__ == '__main__':
    
    print(sum(sieve_E2(2000000))) #ok result: 142913828923
    
    
    