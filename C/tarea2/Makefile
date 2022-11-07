CC=gcc
FLAGS=-Wall 
FLAGS1=-lm -lrt 

all: tarea2 clean

tarea2: code.o sort.o
	$(CC) -o $@ $^ $(FLAGS1)

code.o: code.c
	$(CC) -c $^  $(FLAGS)

sort.o: sort.c
	$(CC) -c $^ $(FLAGS)

code.o: funciones.h
sort.o: funciones.h

clean:
	rm *.o *.gch