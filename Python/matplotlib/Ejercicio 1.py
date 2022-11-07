#lo que hace esta función es leer un archivo y generar listas con los datos del archivo por separado 
def info_temp(archivo):
    try:
        arch = open("temperaturas.txt")
    except Exception:
        raise
    else:
        años = []
        temp = []
        for linea in arch:
            datos = linea.strip().split()
            años.append(datos[0])
            temp.append(datos[1])
        arch.close()
        return [años,temp]


