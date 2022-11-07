def perfect_int():  #easy mode
    flag=True
    while flag==True:
        try:
            x=int(input("Ingrese un numero entero: "))
            flag=False
            return x
        except:
            print("El valor ingresado no es valido. Intentelo de nuevo")
def suma(L): #normal mode
    try:
        t=sum(L)
    except TypeError:
        print("la lista contiene datos no permitidos")
        return -1
    else:
        return t

#easy mode
print(perfect_int()), "\n", print("")

#normal mode
f1=[1 ,2 ,3 ," seiscientos treinta y cinco " ,2.5 , "2.5" , True ]
print(f1), "\n" ,print(suma(f1)), "\n", print("")
f2 =[" quince ", 20 , 12.5 , ".1" , "01"]
print(f2), "\n" ,print(suma(f2)), "\n", print("")
f3 =[10 ,20 ,30 ,50 ,100 ,80 ,70 ,80 ,50 ,30 ,10 ,1]
print(f3), "\n" ,print(suma(f3)), "\n", print("")
input("")