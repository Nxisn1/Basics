def min_max(nombre_archivo, pais):
    arch = open(nombre_archivo)
    PA=[]
    ciu=[]
    aux=[]
    res=[]
    amin=0
    amax=0
    maxp=1
    minp=10000000
    for linea in arch: #para tener solo las ciudades del pais necesario
        linea = linea.strip().split(",")
        if linea[2] == pais:
            PA.append(linea)
    for i in PA: #para saber las ciudades
        if i[1] not in ciu:
            ciu.append(i[1])
    for i in ciu:
        for j in PA:
            if i == j[1]:
                aux.append(j)
                for i in aux:
                    if int(i[3])>int(maxp):
                        maxp=i[3]
                        amax = i[0]
                    if int(i[3])<minp:
                        i[3]=minp
                        amin = i[0]
        a = [i,amin,minp,amax,maxp]
        res.append(tuple(a))
        del aux[:]
    return res


print(min_max('ciudades.txt','United States'))