#normal mode
palabra=("holaaa")
vocales = ["a", "e", "i", "o", "u"]
n = 0
for i in vocales:
    j = palabra.count(i)
    n += j
print(n)
