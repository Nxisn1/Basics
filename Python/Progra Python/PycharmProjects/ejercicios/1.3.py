from math import e, exp
x = 5
n = 5
c=0
fact = 1
z = 1
while z <= n:
    fact*=z
    z = z + 1
print(fact)
print(exp(x))
for i in range(n+1): #0,1,2,3,4,5
    a = x**i
    for j in range(1,n+1): #1,2,3,4,5
        b = fact/j
        c+=b/a
print (exp(x)/fact)
print(c)