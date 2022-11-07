def palindromo(palabra):
    if palabra[::-1] == palabra:
        return(print("es un palíndromo"))
    else:
        return(print("no es na"))
def contador_vocales(palabra):
    a = palabra.count('a')
    e = palabra.count('e')
    i = palabra.count('i')
    o = palabra.count('o')
    u = palabra.count('u')
    return(print(' a =',a,'\n','e =',e,'\n','i =',i,'\n','o =',o,'\n','u =',u,'\n'  ))

palindromo('oso')