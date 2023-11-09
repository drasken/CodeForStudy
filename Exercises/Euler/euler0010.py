"""The sum of the primes below 10  is 2+3+5+7 = 17.

Find the sum of all the primes below two million.

"""

def checkPrimeBrute(num : int) -> bool:
    """
    reutilized from ex 0007
    """
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

indexCheck : int = 2
listSolutions : list = [1]
#too much time to calculate with brute force

# while listSolutions[-1] < 10:
#     if checkPrimeBrute(indexCheck) == True:
#         listSolutions.append(indexCheck)
#     indexCheck += 1

#changed approach, using sieve of Eratostene

#adding only odd numbers
numbersRange : list = [x for x in range(2,2000000) if x % 2 != 0 or x == 2]

#print(numbersRange)
#remove numbers if multiple of another
#it works until 10000
for i in numbersRange:
    for j in numbersRange[1:]:
        if j != i and j % i == 0:
            numbersRange.remove(j)

print (len(numbersRange))
print(numbersRange[-1])

# def trimListPrimes(numbersRange):
#     listPrimesDiscovered : list = [1]
#     for i in numbersRange:
#         pass
        
        

#print(sum(listSolutions[1:-1]))
        
