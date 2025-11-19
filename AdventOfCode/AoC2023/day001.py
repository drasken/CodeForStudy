"""
First day in python
"""


def findStrNum (stringa):
    
    numDicts = {'one' : 1, 'two' : 2, 'three' : 3, 'four': 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}    
    leftIndex = []
    rightIndex = []
    
    for num in numDicts:
        if stringa.find(num):
            leftIndex.append(stringa.find(num))
        if stringa.rfind(num):
            rightIndex.append(stringa.rfind(num))
    
    leftIndex = min(leftIndex)
    rightIndex = max(rightIndex)
    
    newStringa = stringa[:leftIndex] + str(leftIndex) + stringa[leftIndex: rightIndex] + str(rightIndex) + stringa[rightIndex:]
    
    return newStringa
        
    



fileInput = 'input001.txt'
def readTxt(fileName):
    with open(fileName, mode='r') as f:
        results = []
        content = f.readlines()
        print(content[:5])
        for i in range(len(content)):
            content[i] = content[i].removesuffix('\n')
        print(content[:5] + ['secondo print!!!!!!!'])
        for j in content:
            #HERE!!!! add a function that transform the letters in digits
            j = findStrNum(j)
            print(j)
            
            tempWord = ''
            tempList = list(j)
            # print(tempList)
            for k in tempList:
                if k.isdigit():
                    tempWord += k
            results.append(tempWord)
        print(content[:5] + ['terzo print!!!!!!!!'])
        # print(results)
        extract = lambda st : st[0] + st[-1]   #util func for extracting digit 
        results = [extract(x) for x in results]  
        results = [int(y) for y in results]
        #dict to convert string to int for each number
        numDicts = {'one' : 1, 'two' : 2, 'three' : 3, 'four': 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}    

        #return sum(results) -> return for first half
        return content
prova = readTxt(fileInput)
print(prova[:5])

#first output: 54927
#it works!    

