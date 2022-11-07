def Leer_Datos(archivo):
    try:
        arch = open(archivo)
    except FileNotFoundError:
        print("papi eso no existe");raise
    else:
        genero = []
        Getario = []
        Ncont = []
        Rcont = []
        for linea in arch:
            linea = linea.strip().split(';')
            genero.append(linea[0])
            Getario.append(linea[1])
            Ncont.append(linea[2])
            Rcont.append(linea[3])
        arch.close()
        return [genero,Getario,Ncont,Rcont]

# datos = [ [Genero (F o M)] , [Grupo etario (1 = 18-30 )(2 = 31-45 )(3 = 46-64 ) (4 = <= 65)] , [Nueva cont? (1=apr) (2=rech)] ,  [Rcont (1=mixta) (2=const)] ]  
Datos = Leer_Datos("Encuesta.txt")

Genero =  Datos[0]
G_etario = Datos[1]
N_cont = Datos[2]
R_cont = Datos[3]

# Datos ¿Nueva constitución?
#TOTAL_Ncont = len(N_cont)
APRB_Ncont = N_cont.count("1")
RCHZ_Ncont = N_cont.count("2")
x = [[APRB_Ncont],[RCHZ_Ncont]]

# Datos org radacta, C. MIXTA - C. CONST
#TOTAL_Rcont = len(R_cont)
MIX_Rcont = R_cont.count("1")
CONT_Rcont = R_cont.count("2")


#easy mode
def generales(preg1,preg2):
    import matplotlib.pyplot as plt
    sep=0.5
    #TOTAL_Ncont = len(preg1)
    APRB_Ncont = preg1.count("1")
    RCHZ_Ncont = preg1.count("2")
    Apr = 'Aprueba'
    Rch = 'Rechaza'
    #TOTAL_Rcont = len(R_cont)
    MIX_Rcont = R_cont.count("1")
    CONT_Rcont = R_cont.count("2")
    CM = 'C. Mixta'
    CC = 'C. Constitucional'
    sep=0.5
    fig1 = plt.figure(dpi=100)
    fig1.suptitle("Resultados plebiscito", fontsize=16, fontweight="bold")

    ax1 = fig1.add_subplot(1,2,1)
    ax1.bar(Apr,APRB_Ncont,sep,color='skyblue')
    ax1.bar(Rch,RCHZ_Ncont,sep,color="darkred")
    ax1.set_ylabel("Cantidad de votos")

    ax2 = fig1.add_subplot(1,2,2)
    ax2.bar(CM,MIX_Rcont,sep,color='pink')
    ax2.bar(CC,CONT_Rcont,sep,color='greenyellow')

    plt.show()

#easy mode
generales(N_cont,R_cont)

#medium mode
def votos_genero(genero, preg1, preg2):
    VF1=[]
    VM1=[]
    VF2=[]
    VM2=[]
    arch = open('Encuesta.txt')
    for linea in arch:
        linea = linea.strip().split(';')
        if linea[0] == 'F':
            VF1.append(linea[2])
        if linea[0] == 'F':
            VF2.append(linea[3])
        if linea[0] == 'M':
            VM1.append(linea[2])
        if linea[0] == 'M':
            VM2.append(linea[3]) 
    arch.close()
    
    import matplotlib.pyplot as plt
    fig1 = plt.figure(dpi=120)
    fig1.suptitle("Resultado Plebiscito separado por genero", fontsize=14, fontweight="bold")
    
    A1F = VF1.count("1")
    R1F = VF1.count("2")
    size1F = [A1F,R1F]
    etiquetas1F = ["Apruebo","Rechazo"]

    ax1 = fig1.add_subplot(2,2,1)
    ax1.pie(size1F, explode=None, labels=etiquetas1F, autopct="%.0f%%", shadow = True, startangle=90)
    ax1.axis("equal")
    ax1.set_title("Nueva Constitución (Mujeres)")
    

    A1M = VM1.count("1")
    R1M = VM1.count("2")
    size1M = [A1M,R1M]
    etiquetas1M = ["Apruebo","Rechazo"]

    ax2 = fig1.add_subplot(2,2,2)
    ax2.pie(size1M, explode=None, labels=etiquetas1M, autopct="%.0f%%", shadow = True, startangle=90)
    ax2.axis("equal")
    ax2.set_title("Nueva Constitución (Hombres)")


    M2F = VF2.count("1")
    C2F = VF2.count("2")
    size2F = [M2F,C2F]
    etiquetas2F = ["C. Mixta","C. Constitucional"]

    ax3 = fig1.add_subplot(2,2,3)
    ax3.pie(size2F, explode=None, labels=etiquetas2F, autopct="%.0f%%", shadow = True, startangle=90)
    ax3.axis("equal")
    ax3.set_title("Órgano encargado (Mujeres)")
    

    M2M = VM2.count("1")
    C2M = VM2.count("2")
    size2M = [M2M,C2M]
    etiquetas2M = ["C. Mixta","C. Constitucional"]

    ax4 = fig1.add_subplot(2,2,4)
    ax4.pie(size2M, explode=None, labels=etiquetas2M, autopct="%.0f%%", shadow = True, startangle=90)
    ax4.axis("equal")
    ax4.set_title("Órgano encargado (Hombres)")

    plt.show()



votos_genero(Genero,N_cont,R_cont)