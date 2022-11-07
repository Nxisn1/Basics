x=5
N=5
fact = 1
a=0
for i in range(1, N + 1):
    fact *= i
    print(fact)
    for j in range(N + 1):
        a = x ** j
    print(a)