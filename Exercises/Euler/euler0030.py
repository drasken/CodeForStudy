#Find the sum of all the numbers that can be written
#as the sum of fifth powers of their digits.

#max possible number -> 1937102445 9**9 five times
#minimum posible number -> 5 1**1 five times, not good

#use a function to check for each number to see if is valid

def check(number):
    numberStr = str(number)
    listDig = list(numberStr)
    listDig = [int(x) for x in listDig]
    return(sum(listDig))

listRes = []

for i in range(10000, 100000):
    if check(i) == i:
        listRes.append(i)


    
prova = check(132)

print(sum(listRes))

