def pykas_tipo(tipo, archivo):
    try: 
        poke = open('pykadex.csv')

    except Exception:
        print("se ha generado un error")
        raise

    else:
        r = []
        for linea in poke:
            linea = linea.strip().split(',')
            if tipo in linea:
                r.append(linea[1])
        poke.close()

    if len(r) == 0:
        raise ValueError("El tipo de pykamon " + tipo + " no existe")

    return r


def evolucion(pykamon, archivo):
    try:
        poke = open('pykadex.csv')

    except OSError:
        print("se ha generado un error")
        raise

    else:
        evol = []
        for linea in poke:
            linea = linea.strip().split(',')
            if pykamon in linea:
                if linea[4]=='Si':
                    evol.append(linea[5])
                    evol.remove(linea[5])
                    if len(linea)>5:
                        for i in range(5,len(linea)):
                            evol.append(linea[i])

                else:
                    poke.close()
                    return False

        poke.close()  

    if len(evol) == 0 :
        raise ValueError("El pykamon " + pykamon + " no existe")

    return evol


print ( pykas_tipo ("Fuego" ,"pykadex.csv"))
print ( pykas_tipo ("Metal" ,"pykadex.csv"))

print(evolucion("Pykasho"," pykadex.csv"))
print(evolucion("Eevolver"," pykadex.csv"))
print(evolucion("Chorozard"," pykadex.csv"))
print(evolucion("Pysho","pykadex.csv"))