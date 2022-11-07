#otro hard mode
palabra = "para"
list(palabra)
vocales =["a", "e", "i", "o", "u"]
vocales2 = vocales.copy()
p = 0
if "u" in list(palabra):
    #vocales.pop(4)
    list(palabra).remove("u")
    p += 1
if "o" in list(palabra):
    #vocales.pop(3)
    list(palabra).remove("o")
    p += 1
if "i" in list(palabra):
    #vocales.pop(2)
    list(palabra).remove("i")
    p += 1
if "e" in list(palabra):
    #vocales.pop(1)
    list(palabra).remove("e")
    p += 1
if "a" in list(palabra):
    #vocales.remove("a")
    list(palabra).remove("a")
    p += 1
print(p)