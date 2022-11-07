#hardmode
palabra = "holaaa"
t=0
sapo =(list(palabra).pop())
while sapo == "a":
    t+=1
    sapo = (list(palabra).pop())
print(t)