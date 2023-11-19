fib1 = 1
fib2 = 1
ste = 2
while len(str(fib2)) < 1000:
    fib1, fib2= fib2, fib1 + fib2
    step += 1


print(fib2)
print(step)

