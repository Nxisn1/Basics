def suma(L): #normal mode
    try:
        t=sum(L)
    except TypeError:
        print("la lista contiene datos no permitidos")
        return -1
    else:
        return t

f1=[1 ,2 ,3 ," seiscientos treinta y cinco " ,2.5 , "2.5" , True ]
print(suma(f1))

f2 =[" quince ", 20 , 12.5 , ".1" , "01"]
print(suma(f2))

f3 =[10 ,20 ,30 ,50 ,100 ,80 ,70 ,80 ,50 ,30 ,10 ,1]
print(suma(f3))