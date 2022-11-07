def CapturaNumeros(n):
    x=0
    numeros=[]
    while n > x:
        try:
            print("Captura numeros, como ingresaste", n, "Tienes que ingresar", n, "numeros para la lista"); f = float(input("Ingrese un numero entero porfa"))
            numeros.append(f)
            x+=1
        except ValueError:
            print("awnao ingresa numeros validos po")
    return numeros
def Divide_Listas(l1,l2):
    cocientes = []
    for i in l1:
        for n in l2:
            try:
                x = i/n
                cocientes.append(x)
            except ZeroDivisionError:
                print("division por cero? no po papi")
                #return cocientes
    return cocientes

flag = True
while flag:
    try:
        uno = int(input("Ingrese un número entero"))
        flag = False
    except ValueError:
        print("Te dije un número entero... ingresalos de nuevo")

flag = True
while flag:
    try:
        dos = int(input("Ingrese otro número entero"))
        flag = False
    except ValueError:
        print("Te dije un número entero... ingresalos de nuevo")

lista1 = CapturaNumeros(uno); lista2 = CapturaNumeros(dos)
resultados = Divide_Listas(lista1,lista2)
print("La lista 1 es: ", lista1); print("La lista 2 es: ",lista2); print("Los resultados son", resultados)