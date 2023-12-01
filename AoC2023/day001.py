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
        return sum(results)
    
prova = readTxt(fileInput)
print(prova)

#first output: 54927
#it works!    

