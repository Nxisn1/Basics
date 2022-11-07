def division():
    x=int(input("ingrese un dividendo"))
    y=int(input("ingrese un divisor"))
    if y == 0:
        raise ZeroDivisionError("no se puede dividir por 0")
    else:
        return x/y

def division1(x,y):
    try:
        resultado=x/y
        return resultado
    except ZeroDivisionError as v:
        print("no se puede dividir por 0")
        return v
print(division1(4,0))

def indice(x):
    try:
        dig=lista[x]
        return dig
    except IndexError as i:
        print("el rango de la lista es ",len(lista)); print("el índice que pidió no esta en la lista")
        return i

lista=['1','2','3','4','5']
print(indice(9))

def diccionario(x):
    try:
        c=colores[x]
        return c
    except KeyError as k:
        print("ese no está en el diccionario")
        return k

colores = {'rojo':'red','verde':'green','amarillo':'yellow','negro':'black'} #diccionario

t=input("que color quiere traducir?")
print(diccionario(t))