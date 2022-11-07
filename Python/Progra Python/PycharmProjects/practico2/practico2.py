print("Pasopalabra")
palabra=(input("Ingrese una palabra en minusculas: "))
if ("a" or "e" or "i" or "o" or "u" or "á" or "é" or "ó" or "í" or "ú") in palabra:
    easy = palabra.count("a") + palabra.count("e") + palabra.count("i") + palabra.count("o") + palabra.count("u") + palabra.count("á") + palabra.count("é") + palabra.count("í") + palabra.count("ó") + palabra.count("ú")
    print("Easy mode check: OK. Vocales: ", easy)
else:
    print(" Easy mode check: WASTED \n Normal mode check: WASTED \n Hard Mode check: WASTED")
vocales = ["a", "e", "i", "o", "u", "á", "é", "í","ó", "ú"]
if ("a" or "e" or "i" or "o" or "u") in palabra:
    n = 0
    for i in vocales:
        j = palabra.count(i)
        n += j
    print("Normal mode check: OK. Vocales: ", n)
t=0
while len(palabra)/2 != t:
    a = list(palabra).pop()
    if a in ["a","e","i","o","u"]:
        t +=1
print("Hard mode check: OK. Vocales:", t)