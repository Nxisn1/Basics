# JOIN s.join(iterable) basicamente es para convertir listas en str
# 's' es el 'pegamento' o sea con que lo vamos a pegar. en  iterable ponemos la lista.

valores = ["1","2","3","4","5"] 
pegamento = " < "
a = pegamento.join(valores)
print(a); print(type(a))

print(",".join(valores)) #el 'pegamento' se puede poner al principio de join entre comillas o ponerlo en una variable como arriba

print(" 8=D ".join("12345")) #otra forma de ocupar join, poniendo en iterable un str '1 8=D 2 8=D 3 8=D 4 8=D 5'

#INTERPOLACION DE STRING. es una plantilla que se va llenando dinámicamente. los datos se quedan guardados como str
#estencil.format(valor1, valor2, ...)
#ejemplos
s = "Soy {0} y vivo en {1}"; print(s) # este es el estencil, la plantilla. {0} y {1} se llaman 'campos'
print(s.format("jose", "el bosque")) # 'Soy jose y vivo en el bosque'
print(s.format("tulo", "por ahí")) # 'Soy por y vivo en por ahí'

print("{1}{0}{2}{0}".format("a","v","c")) #'vaca'


#campos como identificadores
d = "{nombre} estudia en la {universidad}"; print(d)
print(d.format(nombre = "jose", universidad = "utfsm")) # 'jose estudia en la utfsm'
print(d.format(nombre = "juanin", universidad = "cato de valpo")) #'juanin estudia en la cato de valpo'

#otro ejemplo
s = "estudio en la {0}, en el campus {1}, y vivo en {2}"
a = input("¿Dónde estudias? "); b=input("¿En cuál campus? "); c=input("¿Dónde vives? ")
print(s.format(a,b,c))