def leer_datos(archivo1, archivo2):
    try:
        arch1 = open(archivo1)
        arch2 = open(archivo2)
    except FileNotFoundError:
        print("alguno de los archivos no existe");raise
    else:
        producto = []
        totalV= []
        precio = []
        categoria = []
        for linea in arch1:
            linea = linea.strip().split()
            producto.append(linea[0])
            totalV.append(linea[1])
        arch1.close()
        for linea in arch2:
            linea = linea.strip().split()
            precio.append(linea[1])
            categoria.append(linea[2])
        arch2.close()
        return [producto,totalV,precio,categoria]

L = leer_datos('ventas.txt','datos.txt')
#print(L)

producto = L[0]
totalV= L[1]
precio = L[2]
categoria = L[3]
precioint=[]

TV = []

for i in precio:
    a = int(i)
    
    precioint.append(i)





print(TV)