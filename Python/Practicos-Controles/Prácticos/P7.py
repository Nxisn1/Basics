#Easy mode
def getSpotiPyInfo(filename):
    try:
        arch = open(filename)

    except OSError:
        print("No se puede abrir el archivo")

    else:
        dicc = {}
        for linea in arch:
            linea = linea.strip().split(',')
            dicc[linea[0]]=linea[1:]
        arch.close()
        return dicc

info = getSpotiPyInfo('spotipyData.conf')

#Medium mode
def getGenresData(info, generos, dato='popularidad'):
    try:
        if dato == 'popularidad' or dato == '':
            pop = []
            for i in generos:
                va = info[i]
                va[2] = round(float(va[2]),3)
                pop.append(va[2])
            return([tuple(generos),tuple(pop)])

        elif dato == 'duracion':
            dur = []
            for i in generos:
                va = info[i]
                va[1] = round(float(va[1]),3)
                dur.append(va[1])
            return([tuple(generos),tuple(dur)])

        elif dato == 'bailable':
            bai = []
            for i in generos:
                va = info[i]
                va[0] = round(float(va[0]),3)
                bai.append(va[0])
            return([tuple(generos),tuple(bai)])
        
        else:
            E_dato = "El tipo de dato no es válido"
            return E_dato

    except KeyError:
        E_genero = "Género no válido"
        return E_genero

#Hard mode
def GenerosDatos(info, generos, dato ='popularidad'):
    try:
        from matplotlib import pyplot as plt
        fig = plt.figure(figsize=(8,5),dpi=100)
        fig.subplots_adjust(top=0.9)
        if dato == 'popularidad' or dato == '':
            pop = []
            for i in generos:
                va = info[i]
                va[2] = round(float(va[2]),2)
                pop.append(va[2])

            fig.suptitle("Datos de Spotipy graficados (Popularidad)", fontsize=14, fontweight="ultralight")
            #gráfico 2d
            ax1 = fig.add_subplot(1,2,1)
            ax1.plot(generos,pop,'o-.', color="darkblue", markerfacecolor="red",ms=5, lw=2)
            plt.xlabel("Géneros")
            plt.ylabel("Popularidad")

            #gráfico torta
            ax2 = fig.add_subplot(1,2,2)
            etiquetas = generos
            size = pop
            ax2.pie(size, labels=etiquetas,autopct="%.1f%%", shadow = True, startangle=90)
            ax2.axis("equal")

            plt.show()

        elif dato == 'duracion':
            dur = []
            for i in generos:
                va = info[i]
                va[1] = round(float(va[1]),2)
                dur.append(va[1])

            fig.suptitle("Datos de Spotipy graficados (Duración)", fontsize=14, fontweight="bold")
            #gráfico 2d
            ax1 = fig.add_subplot(1,2,1)
            ax1.plot(generos,dur,'^-', color="skyblue", markerfacecolor="green",ms=7, lw=3)
            plt.xlabel("Géneros")
            plt.ylabel("Duración (milisegundos)")

            #gráfico torta
            ax2 = fig.add_subplot(1,2,2)
            etiquetas = generos
            size = dur
            ax2.pie(size, labels=etiquetas,autopct="%.1f%%", shadow = True, startangle=180)
            ax2.axis("equal")

            plt.show()

        elif dato == 'bailable':
            bai = []
            for i in generos:
                va = info[i]
                va[0] = round(float(va[0]),2)
                bai.append(va[0])

            fig.suptitle("Datos de Spotipy graficados (Bailable)", fontsize=14, fontweight="normal")

            #gráfico 2d
            ax1 = fig.add_subplot(1,2,1)
            ax1.plot(generos,bai,'D--', color="pink", markerfacecolor="cyan",ms=6, lw=4)
            plt.ylim(0,1)
            plt.xlabel("Géneros")
            plt.ylabel("Bailable")

            #gráfico torta
            ax2 = fig.add_subplot(1,2,2)
            etiquetas = generos
            size = bai
            ax2.pie(size, labels=etiquetas,autopct="%.1f%%", shadow = True, startangle=270)
            ax2.axis("equal")

            plt.show()
        
        else:
            E_dato = "El tipo de dato no es válido"
            print(E_dato)

    except KeyError:
        E_genero = "Género no válido"
        print(E_genero)


print(getGenresData(info,['hip hop','korean pop','rap metal']))
GenerosDatos(info,['hip hop','korean pop','rap metal'])
GenerosDatos(info,['hip hop','korean pop','rap metal'],dato='duracion')
GenerosDatos(info,['hip hop','korean pop','rap metal'],dato='bailable')