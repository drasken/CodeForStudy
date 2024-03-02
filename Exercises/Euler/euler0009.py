"""
Pytagorean triplet a<b<c --> a^2 + b^2 = c^2
Ex. 3^2 + 4^2 = 5^2

There exists exactly one Pythagorean triplet for which a+b+c = 1000
Find the product a*b*c
"""
#Problem SOLVED!

#functin to check if triplet is pythagorean
def checkPythagorean(numA, numB, numC):
    if (numA**2) + (numB**2) == (numC ** 2):
        return True
    else:
        return False
   

#function to find triplets for specific sum

def findPytTriplets (limitSum, listRes):
    for numA in range(1, limitSum //2 +1): #enough to check to half + 1
        for numB in range(numA+1, limitSum//2 + 1):
            for numC in range(numB+1, limitSum//2 + 1):
                if numA + numB + numC == limitSum:
                    if checkPythagorean(numA, numB, numC):
                        tripletTuple = (numA, numB, numC)
                        listRes.append(tripletTuple)




if __name__ == '__main__':
    listTri = [] #all triplets
    findPytTriplets(1000, listTri)
    resProduct = lambda x: x[0] * x[1] * x[2]
    result = resProduct(listTri[0]) #It worked!! 
    
    
