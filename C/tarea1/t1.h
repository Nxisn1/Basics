#include<stdio.h>
#include<stdlib.h>
#include<string.h>

FILE *fichero;

typedef struct block{
	char G1, G2, G3, G4;
	struct block *sgte;
} bloque;


typedef struct sample{
	int id;
	bloque *test;
	struct sample *sgte;
} paciente;


typedef struct virus{
	char nom[5];
	bloque *genoma;
} variante;


typedef struct bin_tree{
	variante * nodo;
	int cant;
	struct bin_tree *hijo_izq, *hijo_der;
} arbol;

int lines(const char *arch);
void *nom_V(const char *arch);
void *linea_linea(const char *arch);
int *IDs(const char *arch);
void list_P(paciente **head, int ID, int pos);
void print_list(paciente *head);