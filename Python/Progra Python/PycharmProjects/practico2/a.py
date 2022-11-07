#hard mode
palabra = "para"
vocales =["a", "e", "i", "o", "u"]
vocales2 = vocales.copy()
temp=0
for i in vocales:
    while i in list(palabra):
        list(palabra).remove(i)
        temp +=1
        break
print(temp)
print(list(palabra))