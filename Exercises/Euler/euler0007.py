def checkPrimeBrute(num : int) -> bool:
    """ 
    brute force solution to check if a number is prime
    """
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

indexCheck : int = 2
listSolutions : list[int] = [1]

while len(listSolutions) < 10002:
    if checkPrimeBrute(indexCheck) == True:
        listSolutions.append(indexCheck)
    indexCheck += 1

print(listSolutions[-1])

# Solution 104743
#in spyder it works, in Emacs return an error, don't know why
