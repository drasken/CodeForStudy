"""
2520is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
"""

# DOING

from util import check_if_evely_divisible

listDivisor = [x for x in range(9, 21) if x != 10]

# def divNumbers(num, iterNum):
#     for i in iterNum:
#         if num % i != 0:
#             return False
#     return True

# result = 0

# def checkDiv(index, listIte):
#     newIndex = index
#     tempNum = divNumbers(index, listIte)
#     while tempNum == False:
#         if tempNum == True:
#             break

#         newIndex += index
        
#     return newIndex

# res = checkDiv(indexMax, listDivisor)


# indexRes = 2

# while divNumbers(indexRes, listDivisor) == True:
#     indexRes += 1

# print(indexRes)

if __name__ == '__main__':
    
    test = 11
    firsts = [x for x in range(1,10)]
    while   check_if_evely_divisible(firsts, test) == False:
        test += 1
    
    print(test) #exp 2520 --> OK
    
    count  = 2520
    list_of_divisors = [x for x in range(9, 21) if x != 10]


    while   check_if_evely_divisible(list_of_divisors, count) == False:
        count += 1

    print(count)
    
    #solved --> 232792560

