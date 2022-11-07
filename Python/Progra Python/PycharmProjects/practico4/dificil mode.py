def perfect_int():  #easy mode
    flag=True
    while flag==True:
        try:
            x=int(input("Ingrese un numero entero: "))
            flag=False
            return x
        except:
            print("El valor ingresado no es valido. Intentelo de nuevo")

def reparar(L):
    for i in L:
        try:
            if type(i)==int:
                print("dato correcto")
            if type(i)==float:
                int(i)
                print("dato correcto")
            if type(i)==str:
                int(i)
                print("dato incorrecto, ingrese otro")
        except ValueError:
            perfect_int()

f2 = [" quince ", 20, 12.5, ".1", "01"]
f3 = [10, 20, 30, 50, 100, 80, 70, 80, 50, 30, 10, 1]

#reparar(f3)
reparar(f2)
