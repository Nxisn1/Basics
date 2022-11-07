''' gráfico 1   
    from matplotlib import pyplot as plt
    plt.figure(dpi = 100) #resolución de figura (implica tamaño)
    plt.plot([5,10,15,20],[1,2,3,4]) #el primero para el eje x; el segundo para el eje y
    plt.ylabel("velocidad") #nombre de las variables en el eje y
    plt.xlabel("tiempo") #nombres de las varibales en el eje x
    plt.show() #para mostrar el gráfico '''

''' gráfico 2 
    import matplotlib.pyplot as plt #from matplotlib import pyplot as plt
    plt.figure(dpi=100) #resolución de figura (implica tamaño)
    plt.plot([1,3,4,6,8],[1,16,9,5,3],"ro-") # el "ro-" es para que no sea solo una linea sino que tenga puntos en las coordenadas #se ocupó en el tercer parámetro (ro-) 'r' = red; 'o' circulo; '-' = linea continua
    plt.axis([0,10,0,20]) #[min ejex, max ejex, min ejey, max ejey] #axis es para el max y min de los ejes
    plt.ylabel("Algunos numeritos en el eje y")
    plt.xlabel("Algunos numeritos en el eje x")
    plt.show() '''

''' para personalizar el gráfico
    Marcadores	Descripción

    "."	Punt
    ","	Pixel
    "o"	Círculo
    "^"	Triángulo
    ">"	Triángulo 90º
    "v"	Triángulo 180º
    "<"	Triángulo 270º
    "1"	Ángulo 180º
    "2"	Ángulo
    "3"	Ángulo 270º
    "4"	Ángulo 90º
    "s"	Cuadrado
    "p"	Pentágono
    "*"	Estrella
    "h"	Hexágono 1
    "H"	Hexágono 2
    "+"	Cruz suma
    "x"	Equis
    "D"	Diamante
    "d"	Diamante delgado
    "|"	Línea Vertical
    "_"	Línea Horizontal


    Estilos de Línea	Descripción
    "-"	Línea Continua
    "--"	Línea Segmentada
    "-."	Linea Segmento-Punteada
    ":"	Línea Punteada


    Color	Descripción
    "r" Rojo
    "b"	Azul
    "g"	Verde
    "r"	Rojo
    "c"	Cyan
    "m"	Magenta
    "y"	Amarillo
    "k"	Negro
    "w"	Blanco '''

''' gráfico con varios curvas
    from numpy import arange 
    import matplotlib.pyplot as plt #from matplotlib import pyplot as plt

    t = arange(0.0, 5. , 0.2) #lo mismo que range() pero con floats :o!!! #lo q hace esto es generar una lista (o sea un rango) de floats, el primer valor es la partido, el segundo la llegada y el tercero de cuanto 
                                                                            en cuanto avanza. '[0.  0.2 0.4 0.6 0.8 1.  1.2 1.4 1.6 1.8 2.  2.2 2.4 2.6 2.8 3.  3.2 3.4 3.6 3.8 4.  4.2 4.4 4.6 4.8 ]'   
    print(type(t)) #esto es un array de numpy, soporta floats!

    plt.figure(dpi=100) #resolución de figura (implica tamaño)

    plt.plot(t, t, 'r.--', t, t**2, 'bs-', t, t**3, 'g^:')
    #primeros 3 argumentos: línea roja con puntos y segmentada
    #segundos 3 argumentos: línea azul con cuadrados y continua
    #últimos 3 argumetnos: linea verde con triángulos y punteada

    plt.ylabel("Algunos numeritos en el eje y")
    plt.xlabel("Algunos numeritos en el eje x")
    plt.show()  '''

''' gráfico con más detalles
    from matplotlib import pyplot as plt
    plt.figure(dpi=50)
    plt.plot([1,2,3,4],[1,4,9,16], 'rH-.', color="darkblue", markerfacecolor="green", ms=12, lw=2)
    plt.axis([0,6,0,20]) # los dos primeros son para el eje x; los dos últimos son para el eje y.
    
    para hacer los limites en los ejes por separado
    plt.xlim(0,1)
    plt.ylim(0,1)

    plt.show() '''

''' COLORES para el gráfico con más detalles
    from matplotlib import colors
    for color, hexa in colors.cnames.items():
        print(color, hexa) '''

''' parámetros por defecto
    def maquina(voltaje, ok='funciona', error='falla', tipo="Brazo Robot"):
        if voltaje > 500:
            print("Este", tipo, error, "con", voltaje, "volts.")
        else:
            print("Este", tipo, ok, "con", voltaje, "volts.")
        
        #maquina(800) 'Este Brazo Robot falla con 800 volts.'
        #maquina(voltaje=1000) 'Este Brazo Robot falla con 1000 volts.'
        #maquina(1000,error="WASTED!!") 'Este Brazo Robot WASTED!! con 1000 volts.'
        #maquina(error="Oh s**t, here we go again!", voltaje=1000) 'Este Brazo Robot Oh s**t, here we go again! con 1000 volts.'
        #maquina(100, "funciona!!! AWWWWWWWWW YEEEAAAA", "se detiene") 'Este Brazo Robot funciona!!! AWWWWWWWWW YEEEAAAA con 100 volts.'
        #maquina(490, ok="se mueve, se mueve, se está movieeeeeendo", tipo="Zombie") 'Este Zombie se mueve, se mueve, se está movieeeeeendo con 490 volts.'
        #maquina(ok="Me pasé po...") 'error; porque no tiene el argumento principal(en este caso el voltaje)' '''

'''dos figuras con un gráfico cada una
    import matplotlib.pyplot as plt

    ### figura1
    fig1 = plt.figure(dpi=100)
    ax1 = fig1.add_subplot(1,1,1) #1 fila, 1 columna y gráfico 1.
    ax1.plot([1,2,3,4], [1,4,9,16], 'o--', color="orchid", markerfacecolor="lightgreen", lw=2, ms=10) # 'lw' es para el grosor de la linea y 'ms' para el tamaño de las pelotitas
    ax1.axis([0,5,0,17])

    ### figura2
    fig2 = plt.figure(dpi=100)
    ax2 = fig2.add_subplot(1,1,1) #1 fila, 1 columna y gráfico 1.
    ax2.plot([1,2,3,4], [1,2,3,4], 'v-', color="skyblue", markerfacecolor="magenta", linewidth=3, ms=10)
    ax2.plot([1,2,3,4], [2,4,6,8], 'D-.', color="darkblue", markerfacecolor="violet", lw=2, ms=7)
    #como se definió un solo gráfico, ambas curvas van en el mismo plano.
    ax2.axis([0,6,0,10])

    plt.show() '''

''' una figura con dos gráficos
    import matplotlib.pyplot as plt

    ### figura
    fig1 = plt.figure(dpi = 50)
    ### subgráfico 1
    ax1 = fig1.add_subplot(1,2,1) #1 fila, 2 columna y 1 (sub)gráfico 1. Puede tener 2 (sub)gráficos #aquí en cuantas columnas trabajarás
    ax1.plot([1,2,3,4], [1,4,9,16], 'o--', color="orchid", markerfacecolor="lightgreen")
    ax1.axis([0,6,0,20])

    ### subgrafico 2
    ax2 = fig1.add_subplot(1,2,2) #1 fila, 2 columnas (debe ser igual que lo de arriba) y (sub)gráfico 2. #y aquí lo distinto nomas es el último que indica que trabajarás con el otro gráfico
    ax2.plot([1,2,3,4], [1,2,3,4], 'v-', color="skyblue", markerfacecolor="magenta", linewidth=3)
    ax2.plot([1,2,3,4], [2,4,6,8], 'D-.', color="cyan", markerfacecolor="purple", lw=2)
    #como estamos trabajando en el segundo subgráfico, ambas curvas van en éste.
    ax2.axis([0,6,0,10])

    plt.show() '''

''' textos en gráficos (escribir weas en los gráficos (flechas, titulos, etc.))
    from matplotlib import pyplot as plt

    fig = plt.figure(dpi=100) #50 creo que es muy chico, 100 está bien
    fig.suptitle("Titulo superior en negrita (bold)", fontsize=14, fontweight="bold")

    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85) #ajusta posición de gráfico

    ax.set_title("Titulo de ejes, x vs y") 
    ax.set_xlabel("Etiquta de eje x")
    ax.set_ylabel("Etiquta de eje y")

    #Texto a todo colooooooor!
    ax.text(1.5,8, 'texto a todo color en coordenadas (1.5, 8)', color="darkgreen", fontsize=9)

    #Graficamos un pentagono y una linea segmentada
    ax.plot([2],[1], 'p', ms=10)
    ax.plot([1,2,3,4,5,6,7,8], [0.6,3,2,1,4,5,6,1], 'r--', lw=2)

    # Generamos anotación con una flecha! flecha coordenada (2,1), texto de flecha coordenada (3,1)
    ax.annotate('Acá está el pentagono', xy=(2,1), xytext=(4,7), arrowprops=dict(facecolor='black', shrink=0.05))

    ax.axis([0,10,0,10])
    plt.show() '''

''' gráfico torta
    import matplotlib.pyplot as plt

    #Gráfico de torta; cortes ordenados y gráficados contra reloj.
    etiquetas = ["Ranas","Erizos","Doggos","Gatos"]
    size = [15, 40, 65, 20] 
    explotar = [0, 0, 0.1, 0] #sirve para destacar alguna porcion. El valor es cuanto se separa de la torta.

    fig1 = plt.figure(dpi=100)
    ax1 = fig1.add_subplot(1,1,1) 

    ax1.pie(size, explode=explotar, labels=etiquetas, autopct="%.1f%%", shadow = True, startangle=90)
    # autopct = porcentaje automático; shadow = grafico con sombra; startangle = ángulo de inicio (pa' girarlo)
    # %.2f%% formato de decimal, viene del lenguaje C. Sí, python está escrito en C.

    ax1.axis("equal") #asegura proporcion igualitaria, vale decir, suma de porcentajes 100% (círculo)

    plt.show() '''

''' gráfico de barras 
    import matplotlib.pyplot as plt
    from numpy import arange
    from numpy.random import randint

    fig1 = plt.figure(dpi=100)
    ax1 = fig1.add_subplot(111)

    num = 10
    x = arange(num) #rango de 0 a 10

    ya = randint(0,50,num) #lista de numeros aleatoreos entre 0 y 50
    yb = randint(0,50,num)

    sep = 0.3

    #barras - parametro 1: valores de x; parametro 2: valores en y; parametro 3: ancho de barra.
    ax1.bar(x, ya, sep, color='lightgreen')
    ax1.bar(x+sep, yb, sep, color='darkgreen')

    ax1.set_xticks(x+sep) #posición de etiquetas en x

    ax1.set_xticklabels(list(range(1,num+1))) #nombre de etiquetas en x

    plt.show() '''

''' gráfico histograma (como la wea de la desviación estandar)
    import matplotlib.pyplot as plt
    from numpy.random import seed, randn

    #seed(0) #semilla aleatoria fija, permite generar siempre los mismos números.

    mu = 100 #media
    sigma = 15 #desviación estándar

    #Muestro desde distribución normal (0,1) adaptada a media y dev.est. de nuestro caso
    x = mu + sigma * randn(2000)

    #datos histograma
    num_bins = 50 #casillas/divisiones del histograma
    fig1 = plt.figure(dpi=100)
    ax1 = fig1.add_subplot(1,1,1)

    #Histograma - 1er argumento: datos del muestreo; 2do argumento: numero de divisiones, 3ero: normalizacion.
    #density = True, indica que suma de alturas de las divisiones es 1.
    ax1.hist(x, num_bins, density=True)

    ax1.set_xlabel("IQ")
    ax1.set_ylabel("Probabilidad")
    ax1.set_title("Histograma de IQ")

    plt.show() '''

#para modificar el tamaño del grafico
# fig = plt.figure(figsize=(8,5),dpi=100)