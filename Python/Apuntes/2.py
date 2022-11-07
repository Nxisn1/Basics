hiciste la funcion separar como decia en el ejercicio, abriste el archivo con open y creastes dos listas vacias, una para guardar 
las marcas que cumplian las condiciones de rubro y año y la otra lista para ver que paises eran sin repetir. cambiaste año por anio
por que la ñ no esta en ingles asi que puede traer errores. luego hiciste un for para recorres linea por linea el archivo y le 
haces un strip y split a la coma para que sea una lista luego vefiricaste si el indice coincide con el rubro, si es asi, haces otra condicion
si los 4 caracteres del indice 0 coincide con el año, si cumple las dos condiciones agregas la linea a filtro, ya que en esa lista estaran las marcas
que te interesan. luego cierras el archivo con close.
luego haces un for con repeticion de 10 veces para dejar solo los valores mas grandes de las marcas y asi no tener marcas repetidas
lo hiciste haciendo un for dentro de otro y pusiste unas condiones que si las cumplian removias la lista con el valor menor
luego hiciste otro for en la lista con las marcas con los mayores valores del rubro y el año correspondientes y verificaste el indice 2
que es el del pais, si ya estaba en la lista "paises" pusiste un continue para que siguiera con el proceso, si no es asi lo agregabas a la lista
finalmente hacias un for en la lista de paises, para cada pais creabas un archivo abriendolo y con write para poder modificarlo.
escribiste en el archivo las formalidades y el anio y rubro correspondientes. luego hiciste un for a la lista filtro y si coincidia
que el pais de la lista vista con el pais del  archivo se escribia, escribiste las formalidades, el valor de indice 1 que corresponde a la
marca luego hacias las convercion de miles de dolares y lo escribias en el archivo con el indice 3. asi con cada pais de la lista paises
finalmente cerrabas cada archivo creado con close y retornas el numero de valores de la lista de paises con len, ya que ese es el numero de los 
paises que estan en la lista filtros.



def separar(nombre_archivo, rubro, anio):
    arch = open(nombre_archivo)
    filtro=[]
    paises=[]
    for linea in arch:
        linea = linea.strip().split(",")
        if linea[4] == rubro: #filtro para tener cuales cumplen las condiciones
            if (linea[0][0:4]) == anio:
                filtro.append(linea)
    arch.close()
    for _ in range(10): #filtro para tener los mayores valores
        for i in filtro:
            for j in filtro:
                if i[1]==j[1]:
                    if i[3]>j[3]:
                        filtro.remove(j)
    for i in filtro: #filtros para los paises
        if i[2] in paises:
            continue
        else:
            paises.append(i[2])
    
    for i in paises: #crear los archivos y escribirles los correspondientes
        f = open(i+".txt", "w")
        f.write("Mayor valor en ")
        f.write(anio)
        f.write(" de las marcas del rubro ")
        f.write(rubro)
        f.write(": \n")
        for j in filtro:
            if i == j[2]:
                f.write("Marca: ")
                f.write(j[1])
                f.write(", valor en US$: ")
                us=int(j[3])*1000
                f.write(str(us))
                f.write("\n")
        f.close()
    return len(paises)


print(separar('marcas.txt','Fast-Moving Consumer Goods','2016'))