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

def por_tipo (tipo_prod, datos):
    producto = datos[0]
    totalV= datos[1]
    precio = datos[2]
    categoria = datos[3]
    if tipo_prod in categoria == False:
        raise ValueError("Ese tipo de producto no existe")
    prd_cat = []
    for i in categoria:
        if tipo_prod == i:
            n = categoria.index(i)
            prd_cat.append([producto[n]])
    print(prd_cat)


por_tipo("Abarrotes",L)

             


def compara_tipo(datos):
    #producto = datos[0]
    totalV= datos[1]
    precio = datos[2]
    categoria = datos[3]
    
    
    import matplotlib.pyplot as plt
    fig1 = plt.figure(dpi=100)
    fig1.suptitle("Ventas semanales totales: " , fontsize=14, fontweight="bold")


    ax1 = fig1.add_subplot(1,1,1)
    ax1.pie(size, explode=None, labels=etiquetas, autopct="%.0f%%", shadow = True, startangle=90)
    ax1.axis("equal")

