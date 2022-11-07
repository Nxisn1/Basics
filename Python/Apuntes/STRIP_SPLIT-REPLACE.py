#cuando se hace un strip, split o replace hay que guardarlo en una variable, ya que, estos no modifican el str original, sino que hay que 
# crear uno nuevo


#STRIP apuntes
#chars significa "caracteres" del ingles
#s.strip(<chars>) se pone en "chars" lo que queramos cortar al principio y final de la lista o str. si se omite
#esa parte (s.strip()) eliminará los espacios de mas al principio y al final 
#strip solo sirve para strings (no listas ni nada de eso)

#ejemplo strip
s = "      hola mundo\n           "
a = s.strip()
b = a.strip("h")
print(s)
print(a)
print(b) 
print("www.example.com".strip("wmoc.")) #'expample'
print("www.example.wyz.comw".strip("w")) #'.example.wyz.com' entrega eso, strip solo borra las "w" de los extremos

# strip (saca los espacions del principio y final)

saludo = '             hola            '
saludo_limpio = saludo.strip()
print(saludo) #'            hola      '
print(saludo_limpio) #'hola'






#SPLIT apunte
#Split es para hacer de un str una lista 
#s.split(sep=none,maxsplit=-1) sep es separador y al escribir algo va a separar por cada letra que encuentre si lo omitimos separa por espacios
#y maxsplit indica la cantiidad de separadores máximos. si lo omitimos revisa todo el str

#ejemplo split
s = "ana lavaba las sabanas"; print(s) #lo imprime como str
f = s.split(); print(f) #lo imprime como lista
a = s.split("aba"); print(a)  #lo separa por cada "aba" que encuentre '['ana lav', ' las s', 'nas']' (el separador se borra)

#split (convertir str (o un achivo) a lista) sirv por ejemplo para contar el numero de palabras o para otra cosa que necesites que el archivo sea una lista

ejemplo = 'Mi nombre es jose luis'
l = ejemplo.split() #aqui el separador es el espacio (como no hay nada dentro de los parentesis)
print(l) #'['Mi', 'nombre', 'es', 'jose', 'luis']'

#tambien podemos elegir un separador 
s = ejemplo.split('e')
print(s) #'['Mi nombr', ' ', 's jos', ' luis']'





#REPLACE 
#s.replace(esto,por esto) reemplaza lo que ponemos dentro del parentesis, primero lo que queremos que cambie y luego lo que queremos que salga
orden="Quiero arroz con pollo"; print(orden)
a = orden.replace("arroz","puré"); print(a) 
#replace puede tener un tercer parámetro que indica cuantas veces quiero que se reemplace lo que escribí
rut = "11111111-5"; print(rut) # '11111111-5'
rut2 = rut.replace("1","2"); print(rut2) #'22222222-5'
rut3 = rut.replace("1","2",4); print(rut3) # '22221111-5'
