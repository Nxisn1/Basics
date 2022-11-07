f=open("archivo1.txt","r") #para abrir el archivo

#read
size=10 
print(f.read(size)) read es para que lea una determinada cantidad de caracteres (en este caso 10) 
print(f.read(size)) como esta dos veces va a empezar desde donde quedó en el ultimo read. si no colocamos nada
#en "size", mostrará todo el programa (cuidado con eso por la memoria si el archivo es muy grande) 

#readline (para leer por lineas)
cont=1 #pa contar las lineas
s = f.readline()
while s != "":
    print(cont,s, end="") #el (end="") es para que no se imprima con saltos de linea
    s = f.readline()
    cont+=1
print("")
print("se terminó") 

for lines in f:
    print(cont , lines , end="")
    cont += 1
print("")
print("El nombre es ", f.name)
print("Cerrado?", f.closed)
print("Modo de apertura", f.mode)
f.close() #importantísimo cerrar el programa siempre después de abrirlo 
print("cerrado? ", f.closed)