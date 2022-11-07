#también llamados 'matrices asociativas' son colecciones que relacionan una clave con un valor. son 'mappings'
#el primer valor es la clave, como clave se puede ocupar cualquier valor (int,bool,tuplas) pero no listas o diccionarios
#no tienen orden, no se les accede a sus valores por sus indice, sino que se hace por sus claves. 
#se crean con los parentesis de llave {} o con la funcion dict()
#si la llave no esta en el diccionario ocurre el error KeyError

#ejemplo
diccionario = {"Love Actually":"Richard Curtis", "Kill Bill":"Tarantino", "Amélie":"Jean-Pierre Jeunet"} #esto es un diccionario
#print(diccionario["Kill Bill"]) '“Tarantino'

#se pueden agregar llaves asignandole valor
diccionario["Avengers"] = "Joss Whedon"
print(diccionario)
#si se asigna un valor a una llave que ya existe, esta se sobreescribe. no puede tener llaves repetidas un diccionario
#en cambio el valor si puede estar repetido
del diccionario["Avengers"] #para borrar una llave y un valor 
print(diccionario)


#ejemplo
frut = {'plátano':1.35, 'manzana':0.80, 'pera':0.85, 'naranja':0.70}  #se hace con parentesis de llave {}, las keys (llaves) es lo primero, en este caso las frutas y los 'valores' el precio

frut.items() #para mostrar todo el diccionario (las llaves y sus valores)
frut.keys() #para mostrar las llaves del dict

#frut['Pera'] #para mostar el valor de un elemento
#del frut['Pera'] #para borrar la lleva y el elemento
#frut.clear() #para borrar todo lo del dict

#'Pera' in frut 
#True si esta en el dict y False si es el caso contraio

#frut.get(key,default)	#en key se pone la llave y si existe retorna de lo que pedimos, pero si no existe retorna el mensaje que podemos poner en default

#ejemplo fruta-precio
fruta = input('¿Qué fruta quiere? ')
if (fruta in frut) == True:
    kil = input('cuantos kilos?')
    print("Ud. debe",float(frut[fruta]*float(kil)))
else:
    print("esa wea no la tenemo")

#ejemplo
print(frut.get(fruta,"papi esa wea akí no"))


#ITERACIÓN SOBRE DICCIONARIOS
#for i in diccionario: #entrega las llaves
#    print(i) 'Love Actually', 'Kill Bill', 'Amélie' 

#for i in diccionario.values(): #entrega los valores
#    print(i) 'Richard Curtis', 'Tarantino', 'Jean-Pierre Jeunet'

#ejemplo items()    para ver las llaves y valores del dict
for i, j in diccionario.items():
    print("La película",i,"es del director",j) 


#crear listas de un diccionario
#lista de las llaves:
#print(list(diccionario)) '['Love Actually', 'Kill Bill', 'Amélie']'

#lista de los valores:
#print(list(diccionario.values())) '['Richard Curtis', 'Tarantino', 'Jean-Pierre Jeunet']'

print(len(diccionario)) #entrega el numero de pares de llavers y valores que hay en diccionario
