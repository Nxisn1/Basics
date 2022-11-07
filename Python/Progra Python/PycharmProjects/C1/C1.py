a = ("1. Un excelente comentario.")
b = ("2. Un comentario malísimo.")
c = ("3. No comprendí el mensaje del comentario.")
print("Encuesta del Gobierno de Pyland. \n Sobre ""Larga historia"" del Presidente Nelson \n ¿Qué le pareció el comentario del presidente?: ")
print(a)
print(b)
print(c)
d = int(input("Elija una opción."))
if d == 90:
    print("Opción oculta, por favor vuelva a ingresar la opción oculta.")
while d>3 or d<1:
    d = int(input("Opción invalida, Elija otra opción."))
    if d == 90:
        print("Encuesta finalizada")
        print("No hay encuestados \n Adios.")
        break
print("Opción registrada, gracias por participar.")