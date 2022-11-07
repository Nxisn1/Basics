CC=gcc
FLAGS=-Wall 
FLAGS1=-lm -lrt 

tarea: code.o funciones.o
	$(CC) -o $@ $^ $(FLAGS1)

code.o: code.c
	$(CC) -c $^  $(FLAGS)

funciones.o: funciones.c
	$(CC) -c $^ $(FLAGS)

code.o: t1.h
funciones.o: t1.h


