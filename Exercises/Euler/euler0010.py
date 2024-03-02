"""The sum of the primes below 10  is 2+3+5+7 = 17.

Find the sum of all the primes below two million.

"""

#Using Eratostene method

# allNumbers = [x for x in range(1, 2000001) if x > 2 and x % 2 != 0 and x % 3 != 0 and x % 5 != 0 ] #all number minus even ones, multiple of 3 and 5
# allNumbers = [1,2,3,5] + allNumbers
# allNumbers2 = [x for x in range(1, 2000001) if x > 2 and x % 2 != 0 and x % 3 != 0 and x % 5 != 0 ] #a copy to select
# allNumbers2 = [1,2,3,5] + allNumbers2

resList = [1]

#It became slow, use it to find the first prime up to 100000 and than use that to trim down numbers 
#after that chech if prime for each number
def findPrimes (limit, setResult):
    for num in range(2, limit):
        for eachNum in range(2, num):
            if num % eachNum == 0:
                break
            setResult.add(num)
            
if __name__ == '__main__':
    setPrimes = {1,2}
    findPrimes(10000, setPrimes)
    sumPrimes = sum(setPrimes)
            

# for num in resList:
#     for eachNum in range (2, num):
#         if num % eachNum == 0 :
#             break
#         else:
#             resList.append(num)
        

# listResult = [x for x in range(2,2000) if x % 2 != 0 and x % 3 != 0 and x % 5 != 0 and x % 7 != 0 and x % 11 != 0 and x % 13 != 0 and x % 17 !=0 and x % 19 != 0 and x % 23 != 0 and x % 29 != 0 and x % 31!= 0 and x % 37 != 0]
# listPrimes = [2,3,5,7,11,13,17,19,23,29,31,37] + listPrimes
# index = 0
# for x in listPrimes[index:]:
#     for i in listPrimes[index+1:]:
#         if i % x == 0:
#             listPrimes.remove(i)#print(x)
#     index += 1
# #it works, trimmed a lot of numbers

# #now cycle for to delete number not primes

# for i in listPrimes:
#     for j in listPrimes:
#         if j != i:
#             if j % i == 0:
#                 listPrimes.remove(j)
    


# #print(listPrimes)
# print(sum(listPrimes))
# print(len(listPrimes))


## INSERT HERE FUNCTION USE THIS LOGIC
# CHECK IN THE LIST
# for each number try from the last, if
#               from the start if divido ultimo per primo e dà resto remove() dalla lista

# def checkPrimeBrute(num : int) -> bool:
#     """
#     reutilized from ex 0007
#     """
#     for i in range(2,num):
#         if num % i == 0:
#             return False
#     return True

# indexCheck : int = 2
# listSolutions : list = [1]
# #too much time to calculate with brute force

# # while listSolutions[-1] < 10:
# #     if checkPrimeBrute(indexCheck) == True:
# #         listSolutions.append(indexCheck)
# #     indexCheck += 1

# #changed approach, using sieve of Eratostene

# #adding only odd numbers
# numbersRange : list = [x for x in range(2,2000000) if x % 2 != 0 or x == 2]

# #print(numbersRange)
# #remove numbers if multiple of another
# #it works until 10000
# for i in numbersRange:
#     for j in numbersRange[1:]:
#         if j != i and j % i == 0:
#             numbersRange.remove(j)

# print (len(numbersRange))
# print(numbersRange[-1])

# # def trimListPrimes(numbersRange):
# #     listPrimesDiscovered : list = [1]
# #     for i in numbersRange:
# #         pass
        
        

# #print(sum(listSolutions[1:-1]))
        
