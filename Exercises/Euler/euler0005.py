"""
2520is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20 ?
"""

# DOING


indexMax = 10

listDivisor = [x for x in range(1, indexMax)]

def divNumbers(num, iterNum):
    for i in iterNum:
        if num % i != 0:
            return False
    return True

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


indexRes = 2

while divNumbers(indexRes, listDivisor) == True:
    indexRes += 1

print(indexRes)

