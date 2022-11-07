cont=0
suma=0

while cont <5:
    try:
        x=int(input("ingressa un numero"))
        cont+=1
        suma+=x
    except ValueError:
        print("valor incorrecto")
    except:
        print("error no identificado")
print(suma)