def asientos_disponibles(sala):
    for fila in sala:
        for asiento in fila:
            if asiento=="O":
                return True
    return False

def disponible(fila,asiento,sala):
    if -len(sala)<fila<len(sala):
        if -len(sala[fila])<asiento<len(sala[fila]):
            return sala[fila][asiento]==0

sala = [
["X","X","X","O","O"],
["X","X","X","X","O"],
["X","O","X","O","X"],
["X","X","X","X","O"],
["O","O","X","O","O"],
]


print(sala[0][3])
print(disponible(1,4,sala))