#en otros lenguajes se llamna "arrays" o "vectores" 
#pueden contener cualquier tipo de dato (tmb listas)

#la lista se crean con corchetes [] y se separan por una coma los valores 
#tmb se puede crear ocupando la función 'list' aplicada sobre un iterable
list("hola"), '["h","o","l","a"]'

#INDICES
#se puede acceder a algun elemento de la lista escribiendo el nombre de la lista e indicando el indice del elemento entre corchetes 
lista = [1,2,3,"hola"] #parte del indice 0
#print(lista[0]) '1'

# si en la lista hay otra lista, tenemos que ocupar dos veces los corchetes para acceder a un item de la lista dentro de la otra lista

#se puede modificar un elemento de la lista con esto
lista[0] = 90
#print(lista) '[90, 2, 3, 'hola']'
# si se pone un numero negativo en el indice, este empezara desde atras
#print(lista[-1]) 'hola'
#parte del -1, el -2 es el penultimo y asi sucesivamente

#SLICING
#si queremos una parte de una lista en particular podemos poner un inicio y un final a los corchetes, se tien que separar por dos puntos
#esto creará otra lista
l = lista[0:2]
#print(l) '[90, 2]'

#si escribimos tres numero, el tercero sera de salto, o sea de cuanto en cuanto ira la lista (cada cuantas posiciones agrega el elemento)
l1 = lista[0:4:2]
#print(l1) '[90, 3]'
#si se omite, los por defecto seran el comieno y el final

#con eso tmb se puede ocupar para modificar la lista


#OPERACIONES SOBRE LISTAS
len(lista) #entrega cuantos elementos tiene la lista
lista.append(5) #agrega el elemento al final de la lista
#sum(lista) #entrega la suma de los valores de la lista, tiene que haber solo numeros
# '+'  para concatenar listas 
# '*' para repetir la lista n veces 
# 'in' para saber si un elemento esta en la lista, su contrario es 'not in'. entrega un booleno (True o False)
#print(5 in lista) 'True'
lista.count(5) #cuenta cuantas veces esta el elemento en la lista  
lista.index(5) #entrega el indice en que esta el elemento en la lista 
lista.remove(5)  #elimina el elemento de la lista
del lista[1] #elimina el elemento que esta en ese indice
lista.reverse() #para invertir la lista
#lista.sort() ordena la lista de menor a mayor. tiene que se solo números
#lista.extend("","") #para agregar varios elementos a la lista de una 
#lista.insert(indice,elemento) #para agregar un elemento en un lugar en especifica 
lista.pop() #elimina el primer elemento y lo muestra por pantalla 


#ITERACION SOBRE UNA LISTA
#se puede ocupar un for para recorrer la lisa
for i in lista:
    print(i) #la i pasará por todos los valores de la lista y los mostrará en pantalla 

