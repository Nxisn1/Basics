from math import e, exp
x = 5
N = 5
suma=0
for n in range(N+1):
    s=1
    for i in range (1,n+1):
        s=s*1
    suma=suma+x**n/s
print(suma)