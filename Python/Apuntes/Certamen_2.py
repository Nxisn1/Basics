import math

def obtener_representante(nombre_archivo):
    arch = open(nombre_archivo)
    votos=[]
    for linea in arch:
        linea = linea.split(";")
        votos.append(linea[0])
        if linea[0].lower() != linea[1].lower():
            votos.append(linea[1])
        if linea[0].lower() != linea[2].lower():   
            votos.append(linea[2])
    arch.close()
    ganador=-1
    for i in votos:
        if i.lower() == "andrea campos" or i.lower()=="andrea campos\n" :
            ganador += 1 
    x = (votos[0].upper(),ganador)
    return x 

#print(obtener_representante("votos.txt"))


def filtrar_locales(nombre_archivo, rango):
    arch = open(nombre_archivo)
    tipos=[]
    for linea in arch:
        linea = linea.split(";")
        if linea[1] not in tipos:
            tipos.append(linea[1])
        for i in tipos: 
            i = open(i+".txt", "w")
        
        coo = linea[2].split(",")
        x,y=coo
        if (math.sqrt(int(x)**2+int(y)**2)) <= rango:
            i.write(str(linea))
    arch.close()

filtrar_locales("locales.txt", 10)