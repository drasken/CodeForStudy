# A for Rock, B for Paper, and C for Scissors
#corresponding X for Rock, Y for Paper, and Z for Scissors

#the score for the shape you selected 
#(1 for Rock, 2 for Paper, and 3 for Scissors)
#plus the score for the outcome of the round 
#(0 if you lost, 3 if the round was a draw, and 6 if you won).

with open(file="input02A.txt", mode="r") as file:
    stringaS = file.readlines()
    responses = []
    res = 0
    for i in stringaS:
        responses.append(i[2:].rstrip("\n")) #only letter for response

    for k in responses: #this cycle count the points of response signs
        if k == 'X':
            res += 1
        elif k == 'Y':
            res += 2
        elif k == 'Z':
            res += 3
#still miss points draws and wins

   

    #res1 = 41566, wrong too high
    #res2 = 20938, wrong too high