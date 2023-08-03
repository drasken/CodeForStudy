with open (file="input01A.txt", mode="r") as file:
    nums = file.readlines()
    count = []
    temp = 0
    for i in nums:
        if i != "\n":
            temp += int(i.removesuffix("\n"))
        else:
            count.append(temp)
            temp = 0
    #solutino for first half
    new_count = sorted(count, reverse=True)
    
    print(sum(new_count[0:3]))


    #solutionA 72511
    #OK!!

    #solution B1 142325, too low...
    #solution B2 212117
    #OK!!