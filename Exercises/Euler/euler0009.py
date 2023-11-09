"""
Pytagorean triplet a<b<c --> a^2 + b^2 = c^2
Ex. 3^2 + 4^2 = 5^2

There exists exactly one Pythagorean triplet for which a+b+c = 1000
Find the product a*b*c
"""

def checkPythagorean(numA, numB, numC):
    sommaSquare = numA ** numA + numB ** numB
    if sommaSquare == numC ** numC:
        return numA,numB,numC
    else:
        return 0
    
triSum = 1000

indexA,indexB,indexC = 0,0,0

def findTriplets(limitSum, num1, num2, num3):
    checkFunc = checkPythagorean(num1, num2, num3)
    if checkFunc == limitSum:
        return num1* num2 * num3
    else:
        return -1
    
