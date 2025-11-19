with open ("input001.txt") as f:
    content = [x.strip().split() for x in  f.readlines()]
    #test
    content = [(int(x[0]), int(x[1])) for x in content]
    
    print("content iniziale")
    print(content[:10])
    firsts = list()
    seconds = list()

    for p in content:
        firsts.append(p[0])
        seconds.append(p[1])
        
    firsts = sorted(firsts)
    print("test 1")
    print(firsts[:10])
    seconds = sorted(seconds)
    print("test 2")
    print(seconds[:10])
    
    calc_list = [(x * seconds.count(x)) for x in firsts]
    
    print("test 3")
    print(calc_list[:10])
    
    resul = sum(calc_list)
    print(resul)
    
"""
Code for  Part ONE

    thrd = list()
    thrd2 = list(zip(seconds, firsts))
    print("test 3")
    print(thrd2[:10])

    thrd2 = [ abs((x[0] - x[1])) for x in thrd2]
    
    for num, el in enumerate(seconds):
        res = int(el) - int(firsts[num])
        thrd.append(res)

    print(thrd[:10])
    print(thrd2[:10])

    result = sum(thrd)
    result2 = sum(thrd2)

    print(result)
    print(result2)
                  

    ## 1054121: not right, too low
    ## 1506483: OK!!!
        
"""
    



