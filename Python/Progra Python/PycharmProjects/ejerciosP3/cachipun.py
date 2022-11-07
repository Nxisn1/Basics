print("bienvenido a cachipum el que gane 3 rondas sera el pussy-destroyer")
pj1=0
pj2=0
while pj1 or pj2 != 3:
    j1 = input("jugador 1 Escribe tu jugada (piedra,papel o tijera)")
    j2 = input("jugador 2 Escribe tu jugada (piedra,papel o tijera)")
    if j1=="piedra" and j2=="papel":
        pj2+=1
        print("ganador j2")
        print("puntaje jugador 1:",pj1, '\n'  "puntaje jugador 2:",pj2)
    elif j1=="piedra" and j2=="tijera":
        pj1+=1
        print("ganador j1")
        print("puntaje jugador 1:", pj1, '\n'  "puntaje jugador 2:", pj2)
    elif j1=="papel" and j2=="piedra":
        pj1+=1
        print("ganador j1")
        print("puntaje jugador 1:", pj1, '\n'  "puntaje jugador 2:", pj2)
    elif j1=="papel" and j2=="tijera":
        pj2+=1
        print("ganador j2")
        print("puntaje jugador 1:", pj1, '\n'  "puntaje jugador 2:", pj2)
    elif j1=="tijera" and j2=="piedra":
        pj2+=1
        print("ganador j2")
        print("puntaje jugador 1:", pj1, '\n'  "puntaje jugador 2:", pj2)
    elif j1=="tijera" and j2=="papel":
        pj1+=1
        print("ganador j1")
        print("puntaje jugador 1:", pj1, '\n'  "puntaje jugador 2:", pj2)
    else:
        print("empate")
        print("puntaje jugador 1:", pj1, '\n'  "puntaje jugador 2:", pj2)

if pj1==3:
    print("pussy-destroyer = jugador 1")
if pj2==3:
    print("pussy-destroyer = jugador 2")
