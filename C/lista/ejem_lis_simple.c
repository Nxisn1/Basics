#include<stdlib.h>
#include<stdio.h>

typedef struct nodo{
	int dato;
	struct nodo *sgte;
} nodo_t;


void crear_nodo(nodo_t **cabeza, int dato, int pos){

	nodo_t * nuevo = malloc(sizeof(nodo_t));
	nodo_t * recorredor = (*cabeza);
	int cont;

	if (nuevo == NULL){
		printf("Error en la creacion de nodo\n");
		exit(-1);
	}

	nuevo->dato = dato;
 
	if(recorredor==NULL || pos==0){ //casos primer nodo
		nuevo->sgte = (*cabeza);
		*cabeza = nuevo;
	}else{ //caso entre nodos y final
		for (cont=0; cont<pos-1;cont++){
			if(recorredor->sgte==NULL) //para nodo final
				break;
			recorredor = recorredor->sgte;
		}
		nuevo->sgte = recorredor->sgte;
		recorredor->sgte = nuevo;
	}
}


void print_list(nodo_t *cabeza){
	int pos;
	nodo_t * recorredor = cabeza;

	printf("Imprimiendo lista\n");
	for(pos=0; recorredor!=NULL; pos++){
		printf("Lista pos: %d, valor: %d\n", pos, recorredor->dato);
		recorredor = recorredor->sgte;
	}

	printf("\n\n");
}


int list_len(nodo_t *cabeza){
	int cont;
	nodo_t *recorredor = cabeza;
	for(cont=0;recorredor != NULL; cont++){
		recorredor = recorredor->sgte;
	}

	return cont;
}


void clean_list(nodo_t *cabeza){
	nodo_t *recorredor = cabeza;
	while(recorredor!=NULL){
		cabeza = recorredor->sgte;
		free(recorredor);
		recorredor=cabeza;
	}
}


int main(int argc, char **argv){
	
	nodo_t *inicio = NULL;

	crear_nodo(&inicio, 5, 10);
	print_list(inicio);

	crear_nodo(&inicio, 10, 10);
	print_list(inicio);
	
	crear_nodo(&inicio, 200, 1);
	print_list(inicio);
	
	crear_nodo(&inicio, 0,0);
	print_list(inicio);
	
	crear_nodo(&inicio, 555, 4);
	print_list(inicio);
	
	crear_nodo(&inicio, 666, 4);
	print_list(inicio);

	printf("Largo lista: %d\n", list_len(inicio));

	clean_list(inicio);
	
	return 0;
}

