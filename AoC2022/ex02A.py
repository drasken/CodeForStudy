# A for Rock, B for Paper, and C for Scissors
#corresponding X for Rock, Y for Paper, and Z for Scissors

#the score for the shape you selected 
#(1 for Rock, 2 for Paper, and 3 for Scissors)
#plus the score for the outcome of the round 
#(0 if you lost, 3 if the round was a draw, and 6 if you won).

with open(file="input02A.txt", mode="r") as file:
    stringaS = file.readlines() #the string read from the txt file
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

    points_game = []
    for j in stringaS:
        points_game.append(j.rstrip("\n"))

    for n in points_game:#this cycle count the points for each game
        if n == "A X" or n == "B Y" or n =="C Z":
            res += 3
        elif n == "A Y" or n == "B Z" or n == "C X":
            res += 6
        else:
            continue            

    print(res)

    #res1 = 41566, wrong too high
    #res2 = 20938, wrong too high
    #res3 = 12535 OK!!
    
    #SECOND PART
    """
    The Elf finishes helping with the tent and sneaks back over to you. 
    "Anyway, the second column says how the round needs to end: 
    X means you need to lose, Y means you need to end the round in a 
    draw, and Z means you need to win. Good luck!"
    """
