#tuple. en otros lenguajes se les llama 'registros'
#varias cosas de la lista se aplica tmb para las tuplas
#son inmutable (que no se pueden modificar)
#ocupan menos memoria que las listas

#la tuplas se hacen con parentesis normales '()' y se separan los elementos con comas
#una tupla con un solo elemento teneemos que ponerle una coma por lo menos, por que si no, no la reconocera como tal
t = (1); tp = (1,)
#print(type(t), type(tp)) 'class int' 'class tuple'

#para referirnos a un elemento de la tupla, igual que en la lista , se ocupa los corchetes []

#DESEMPAQUETADO DE TUPLAS 
#recuperar los valores de la tupla 
persona = ("Perico" , "Jara")
nombre, apellido = persona # nombre == 'Perico', apellido == 'Jara'
#aveces no nos interesan todos los valores de la tupla por lo que 'desenpacamos' algunas nomas
persona = ("Perico Jara", '8395188-5', (1980, 5 , 14))
_,_,(_,mes,_) = persona #asi solo obtenemos el que no interese 
#print(mes) '5'

#COMPARACIÓN DE TUPLAS
#Dos tuplas son iguales cuando tienen el mismo tamaño y cada uno de sus elementos correspondientes tienen el mismo valor
#print((1,2) == (3//2, 1+1)) 'True'

#para determinar si una tupla es menor que otra. si los elementos en la primera posicion de ambas tuplas son distintos, ellos determinan el orden de las tuplas 
#si son iguales los primeros, ocupa los siguientes, asi hasta que sean distintos y hace la comparacion
#tupla con menor elementos tmb es menor

#las fechas se guardan en tuplas (año,mes,dia) este orden es para saber el orden en que ocurrieron

#Ejemplo de unpack
alumnos = [
('Perico', 'Los Palotes', '201199001-5', 'Civil'),
('Fulano', 'De Tal', '201199002-6', 'Electrica'),
('Fulano', 'De Tal', '201199003-7', 'Mecanica'),
]

for nombre, apellido,rol,carrera in alumnos:
    print(nombre,"estudia",carrera)

for nombre,_ ,_ ,carrera in alumnos:
    print(nombre,"estudia",carrera) #lo mismo que arriba solo que mas acortado ya que no nos interesa ni su apellido ni su rol


#ITERACION SOBRE TUPLAS 
#se puede tranformar una lista a tupla ocupando el 'tuple' sobre la lista y viceversa utilizando el 'list' sobre la tupla
