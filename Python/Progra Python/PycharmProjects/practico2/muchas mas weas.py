#hardmode
palabra = "paralelepipedo"
t=0
while len(palabra)/2 != t:
    a = list(palabra).pop()
    if a in ["a","e","i","o","u"]:
        t +=1
print(t)