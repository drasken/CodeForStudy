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

numbersRange : list = [x for x in range(2000000)]

def trimListPrimes(numbersRange):
    listPrimesDiscovered : list = [1]
    for i in numbersRange:
        pass
        
        

print(sum(listSolutions[1:-1]))
        
