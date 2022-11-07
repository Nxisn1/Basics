Asignaturas=["Matemáticas", "Física", "Química", "Historia", "Lengua"]
Reprobadas=[]
for i in Asignaturas:
    a = int(input("que nota sacaste en " + i + "?"))
    if a < 55:
        Reprobadas.append(i)
if len(Reprobadas) == 5:
    print("te echaste todo...")
else:
    print("aweonao reprobaste " + str(Reprobadas))