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
    print(max(count))
    
    #soluzione 72511
    #OK!!