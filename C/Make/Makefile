CC=gcc
FLAGS=-Wall 
FLAGS1=-lm -lrt 

all: TEST clean exe

TEST: main.o funcion.o
	$(CC) -o $@ $^ $(FLAGS1)

main.o: main.c
	$(CC) -c $^  $(FLAGS)

funcion.o: funcion.c
	$(CC) -c $^ $(FLAGS)

main.o: main.h
funcion.o: main.h

clean:
	rm *.o *.gch

exe:
	./TEST "Probando el make"

