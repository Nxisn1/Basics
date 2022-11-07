#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct nodo_pila{

	char letra;
	struct nodo_pila *sgte;
}pila_t;

void push(pila_t **tope, char dato){ //por referencia porque tiene q cambiar

	pila_t *nuevo = malloc(sizeof(pila_t));
	nuevo->letra = dato;
	nuevo->sgte = *tope;
	*tope = nuevo;
}

char pop(pila_t **tope){
	pila_t *objetivo = *tope;
	char valor = objetivo->letra;
	*tope = objetivo->sgte; //es el mismo que (*tope)->sgte
	
	free(objetivo);

	return valor;	
}

int is_empty(pila_t *tope){
	if(tope==NULL)
		return 1;
	
	return 0;
}

char peak(pila_t *tope){
	return tope->letra;
}

void clear(pila_t **tope){
	pila_t *objetivo = *tope;
	while(objetivo!=NULL){
		*tope = objetivo->sgte;
		free(objetivo);
		objetivo = *tope;
	}
}

char *dar_vuelta(char *palabra){
	int i;
	pila_t *stack= NULL;
	for(i=0;i<strlen(palabra);i++){
		push(&stack, palabra[i]);
	}
	
	char *flip;
	flip = malloc(sizeof(char) * (strlen(palabra)+1));

	for(i=0;i<strlen(palabra);i++){
		sprintf(flip, "%s%c", flip, pop(&stack));
	}
	if(!is_empty(stack))
		clear(&stack);

	return flip;
}

int main(int argc, char **argv){

	if(argc!=2){
		printf("ingrese cantidad correcta de parametros\n ./Binario string o ./Binario \"string\" \n");
		return -1;
	}
	char *string = argv[1];
	char *inv = dar_vuelta(string);
	
	printf("el string es invertido es %s\n", inv);
	free(inv);

	return 0;
}
