"""
Find the sum of the digits in the number 100!.
"""

def factorial(num):
    start = 1
    res = 1
    while start != num:
        res *= start
        start += 1
    return res

partFact = factorial(101)

partRes = str(partFact)

partRes = sum([int(x) for x in partRes])
print(partRes)
        
#it works
