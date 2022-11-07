def getDivisoresPropios(num):
    if type(num) != int:
        raise NameError("El parámetro no es un numero entero")
    if num <= 1:
        raise ValueError("El parámetro debe ser mayor que 1")
    divisores = []
    for i in range(1,num):
        if num % i == 0:
            divisores.append(i)
    return divisores
    #ejemplos
    #print(getDivisoresPropios(10));print(getDivisoresPropios(42));print(getDivisoresPropios(0));print(getDivisoresPropios("pez"))
def SonAmigos(num1,num2):
    try:
        div1 = getDivisoresPropios(num1)
        div2 = getDivisoresPropios(num2)
        if sum(div1) == num2 and sum(div2) == num1:
            return True
        return False
    except:
        print("se produjo un error en SonAmigos")
        raise
    #ejemplos
    #print(SonAmigos(220,240));print(SonAmigos(284,220));print(SonAmigos("p","q"))
def EsPerfecto(num):
    try:
        div = getDivisoresPropios(num)
        if sum(div) == num:
            return True
        return False
    except:
        print("Se produjo un error en EsPerfecto")
        raise
    #ejemplos
    #print(EsPerfecto(10));print(EsPerfecto(6));print(EsPerfecto("pez"))
def getAmigos(nmin,nmax):
    ga = []
    try:
        for i in range(nmin,nmax+1):
            d = getDivisoresPropios(i)
            suma = sum(d)
            if suma>i and suma>=nmin and suma<=nmax and SonAmigos(i,suma):
                f.append([i,suma])
    except Exception as e:
        print("se ha generado un error", type(e))
        return e
    else:
        return f
    #ejemplos
    #print(getAmigos(2,2000));print(getAmigos("pez","gato"));#print(SonAmigos(-10,2000))
def getPerfectos(nmin,nmax):
    gp = []
    try:
        for i in range(nmin,nmax):
            if EsPerfecto(i):
                gp.append(i)
    except Exception as e:
        print ("se ha producido un error", type(e))
        return e
    else:
        return gp
    #ejemplos
    #print(getPerfectos(2,2000));print(getPerfectos("p","q"));print(getPerfectos(-10,2000))