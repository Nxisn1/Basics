def initVotos(cand):
    try:
        arch = open(cand)
    except OSError:
        E_a = "No se puede abrir el archivo. Inténtelo nuevamente"
        return E_a
    else:
        dic = {}
        for linea in arch:
            linea = linea.strip().split()
            dic[linea[0]]= 0
        arch.close()
        return dic


pizarra = initVotos("candidatos.txt")

def cuentaVotos(pizarra, comentarios):
    try:
        arch_C = open(comentarios)
    except OSError:
        E_a = "No se puede abrir el archivo. Inténtelo nuevamente"
        return E_a
    else:
        for linea in arch_C:
            linea = linea.replace(',', '')
            linea = linea.strip().split()
            if "#elecciones_ceetel" in linea:
                for i in pizarra:
                    if i in linea:
                        pizarra[i] = pizarra[i]+1
        return pizarra

pizarra = cuentaVotos(pizarra,"pybook.txt")

def resultadosVotos(pizarra):
    from matplotlib import pyplot as plt
    
    keys = list(pizarra.keys())
    values = list(pizarra.values())

    fig = plt.figure(figsize=(10,6),dpi=100)
    a = values.index(max(values))
    b = keys[a]
    tilt = "Resultados elecciones CEETEL", ' Total votos: ', sum(values), "Ganadora lista de Presidente: ", b
    fig.suptitle(tilt, fontsize=14, fontweight="ultralight")

    etiquetas = keys
    size = values
    explotar = (0.15, 0, 0, 0, 0)


    plt.pie(size, explode=explotar, labels=etiquetas,autopct="%.1f%%", shadow = True, startangle=90)
    plt.axis("equal")

    plt.show()



    

resultadosVotos(pizarra)