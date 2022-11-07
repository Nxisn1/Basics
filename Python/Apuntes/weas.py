arch = open("ciudades.txt")
pais = "United States"
PA=[]
ciu=[]
aux=[]
res=[]
amin=0
amax=0
maxp=1
minp=10000000
for linea in arch:
    linea = linea.strip().split(",")
    if linea[2] == pais:
        PA.append(linea)
for i in PA:
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
            res.append(tuple(i," ",amin," ",minp" ",amax" ",maxp))
            del aux[:]
            







