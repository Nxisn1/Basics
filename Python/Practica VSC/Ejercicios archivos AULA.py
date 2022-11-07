def num_lineas(archivo):
    try:
        arch = open(archivo)
    except OSError as e:
        print("error")
        return e
    else:
        cont=0
        for linea in arch:
            cont+=1
        arch.close()
        return cont
    #ejemplo print(num_lineas2('el quijote.txt'))

def num_palabras(archivo):
    try:
        arch = open(archivo)
    except OSError as e:
        print("error")
        return e
    else:
        total_p = 0
        for linea in arch:
            linea = linea.split()
            total_p += len(linea)
        arch.close() #acuedate de cerrar la wea
        return total_p
    #print(num_palabras('el quijote.txt'))

def num_letras(archivo):
    try:
        arch = open(archivo)
    except OSError as e:
        print("error")
        return e
    else:
        total = 0
        for linea in arch:
            linea = linea.split()
            for i in linea:
                total += len(i)
        arch.close()
        return total

#print('el número de lineas es:',num_lineas('el quijote.txt'))
#print('el número de palabras es:',num_palabras('el quijote.txt'))
#print('el número de letras es:', num_letras('el quijote.txt'))


def aprobados(archivo):
    try:
        arch = open(archivo)
        salida = open('aprobados.txt', 'w')
    except OSError:
        print("hubo un error")
        raise
    else:
        for linea in arch:
            datos = linea.split(':')
            prom = round((int(datos[2])+int(datos[3])+int(datos[4]))/3)
            datos = datos[:2]
            datos.append(str(prom))
            if prom >= 55:
                salida.write(','.join(datos)+'\n')
        arch.close()
        salida.close()

#aprobados('alumnos.txt') #para que se cree el archivo

def reprobrados(archivo):
    try:
        arch = open(archivo)
        salida = open('reprobados.txt', 'w')
    except OSError:
        print("hubo un error")
        raise
    else:
        for linea in arch:
            datos = linea.split(':')
            prom = round((int(datos[2])+int(datos[3])+int(datos[4]))/3)
            datos = datos[:2]
            datos.append(str(prom))
            if prom <= 54:
                salida.write(','.join(datos)+'\n')
        arch.close()
        salida.close()

#reprobrados('alumnos.txt') #para que se cree el archivo


def estadistica_curso(archivo):
    try:
        arch = open('Alumnos.txt')
        output = open('estadistica.txt','w')
    except OSError:
        print("algo ha salido mal")
        raise
    else:
        stats=[[],[],[],[]]
        for linea in arch:
            datos=linea.strip().split(":")
            prom=round((int(datos[2])+int(datos[3])+int(datos[4]))/3)
            stats[0].append(int(datos[2]))
            stats[1].append(int(datos[3]))
            stats[2].append(int(datos[4]))
            stats[3].append(prom)
        arch.close()
        output.write("Alumnos inscritos: "+str(len(stats[0]))+"\n")
        cont=0
        for nota in stats[3]:
            if nota>=55:
                cont+=1
        output.write("Cantidad de aprobados: "+str(cont)+"\n")
        output.write("Cantidad de aprobados: "+str(len(stats[3])-cont)+"\n")
        c=1
        s="Stats {0} - Prom: {1}, DE:{2}, Apro:{3}%, Repro:{4}%\n"
        for act in stats:
            cont=0
            prom=round(sum(act)/len(act))
            de=0
            for nota in act:
                de+=(nota-prom)**2
                if nota>=55:
                    cont+=1  
            de= round((de/(len(act)-1))**0.5,2)
            apro = cont
            papro = round(cont/len(act)*100,2)
            prepro = 100-papro
            ev="C"+str(c) if c<4 else "Final"
            output.write(s.format(ev,prom,de,papro, prepro))
            c+=1
        output.close()
