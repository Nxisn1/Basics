user = ['juan','pedro','alejandro','jose','pepe','marcelo','eduardo']

flag=True
while flag:
    a = input("Ingrese nombre que quiera agregar a usuarios: ")
    try:
        if a in user:
            raise ValueError("ya está po papi")
    except ValueError as v:
        print(v)
    else:
        user.append(a)
        print("El nombre fue agregado correctamente")
    finally:
        b = input("Quiere continuar? y/n: ")
    
    if b == "n":
        flag=False


print("los usuarios son", user)
print("la cantidad de usuarios es", len(user))
