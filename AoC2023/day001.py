"""
First day in python
"""

fileInput = 'input001.txt'
def readTxt(fileName):
    with open(fileName, mode='r') as f:
        results = []
        content = f.readlines()
        for i in range(len(content)):
            content[i] = content[i].removesuffix('\n')
        for j in content:
            tempWord = ''
            tempList = list(j)
            for k in tempList:
                if k.isdigit():
                    tempWord += k
            results.append(tempWord)
        extract = lambda st : st[0] + st[-1]   #util func for extracting digit 
        results = [extract(x) for x in results]  
        results = [int(y) for y in results]
        #dict to convert string to int for each number
        numDicts = {'one' : 1, 'two' : 2, 'three' : 3, 'four': 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}    

        #return sum(results) -> return for first half
        return content
prova = readTxt(fileInput)
print(prova)

#first output: 54927
#it works!    

