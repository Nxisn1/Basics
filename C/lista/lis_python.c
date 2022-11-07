#include<stdio.h>
#include<stdlib.h>

typedef struct nodo{
	int dato;
	struct nodo *sgte;
} nodo_t;

void add_node(nodo_t **head, int datinho, int pos){

	nodo_t *nuevo = malloc(sizeof(nodo_t)); //crea la caja
	nuevo->dato = datinho;

	if(nuevo==NULL){ //por si el malloc no funciona
		printf("error de asiganción de memoria\n");
		exit (-1);
	}

	if(*head==NULL || pos==0){
		nuevo->sgte = *head;
		*head = nuevo;
	
	}else{

		nodo_t *rec = *head;
		int cont;

		for(cont=0; cont<pos-1;cont++){
			if(rec->sgte == NULL){
				break;
			}
			rec = rec->sgte; 	
		}
		nuevo->sgte = rec->sgte;
		rec->sgte = nuevo;

	}

}

void print_list(nodo_t *head){

	nodo_t *rec = head;
	printf("[");
	while(rec!=NULL){
		printf("%d ", rec->dato);
		rec = rec->sgte;
	}
	printf("]\n"); 
}

void clear_list(nodo_t *head){
	nodo_t *rec = head;
	while(rec!=NULL){
		head = head->sgte;
		free(rec);
		rec = head;
	}
}

int len_list(nodo_t *head){
	int cont=0;
	nodo_t *rec = head;
	while(rec!=NULL){
		cont++;
		rec = rec->sgte;	
	}
	return cont;
}

void del_nodo(nodo_t **head,int pos){ //como esta pasado por referencia tmb cambia fuera de la funcion
	nodo_t *objetivo = *head;

	if(objetivo==NULL){
		printf("no se puede borrar elemento de lista vacia\n");
	}else if(pos==0){
		*head = objetivo->sgte;
		free(objetivo);
		objetivo=NULL;
	}else{
		nodo_t *rec = *head;
		int cont;
		for(cont=0; cont<pos-1; cont++){
			rec = rec->sgte;
		}
		objetivo = rec->sgte;
		rec->sgte = objetivo->sgte;
		free(objetivo);
		objetivo=NULL;
	}
}

int main(int argc, char **argv){

	nodo_t *inicio = NULL;

	add_node(&inicio, 1, 0); //1
	print_list(inicio);
	add_node(&inicio, 5, 1); //1,5
	print_list(inicio);
	add_node(&inicio, 3, 1); //1,3,5
	print_list(inicio);
	add_node(&inicio, 2, 1); //1,2,3,5
	print_list(inicio);
	add_node(&inicio, 4, 3); //1,2,3,4,5
	print_list(inicio);

	add_node(&inicio,90,100); //1,2,3,4,5,90
        print_list(inicio);
	
	printf("El largo de la lista es: %d\n", len_list(inicio));
	
	del_nodo(&inicio, 0); //2,3,4,5,90
	del_nodo(&inicio, 2); //2,3,5,90
	print_list(inicio);
	clear_list(inicio);	

	return 0;
}
