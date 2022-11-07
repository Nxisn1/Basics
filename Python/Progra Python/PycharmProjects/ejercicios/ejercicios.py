vocales = ["a","e","i","o","u"]
palabra = input("escribe alguna wea ")
for i in vocales:
    veces = 0
    for letra in palabra:
        if letra == i:
            veces += 1
    print("la  vocal " + i + " aparece " + str(veces))