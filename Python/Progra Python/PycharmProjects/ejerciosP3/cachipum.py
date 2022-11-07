def cachipum(j1,j2): #piedra,papel,tijera
    pj1 = 0;pj2 = 0
    if j1=="piedra":
        if j2=="papel":
            pj2+=1
        elif j2=="tijera":
            pj1+=1
    if j1 == "papel":
        if j2 == "tijera":
            pj2 += 1
        elif j2 == "piedra":
            pj1 += 1
    if j1 == "tijera":
        if j2 == "piedra":
            pj2 += 1
        elif j2 == "papel":
            pj1 += 1
    if j1==j2:
        print("empate")

pj1=0;pj2=0
while pj1 or pj2 != 3:
    j1 = input("jugador 1 Escribe tu jugada (piedra,papel o tijera)")
    j2 = input("jugador 2 Escribe tu jugada (piedra,papel o tijera)")
    cachipum(j1,j2)