#include<stdio.h>
#include<stdlib.h>

typedef struct nodo{
	int dato;
	struct nodo *hijo_izq;
	struct nodo *hijo_der;
}nodo_t;

void insert(nodo_t **raiz, int value){
	if(*raiz==NULL){
		*raiz = malloc(sizeof(nodo_t));
		
		if(*raiz==NULL){
			printf("Falla de malloc...\n");
			exit(-1);
		}
	(*raiz)->dato = value;
	(*raiz)->hijo_izq = NULL;
	(*raiz)->hijo_der = NULL;
	}else if(value <= (*raiz)->dato){
		insert(&((*raiz)->hijo_izq), value);

	}else if(value > (*raiz)->dato){
		insert(&((*raiz)->hijo_der), value);
	 }
	
}

void clear(nodo_t *raiz){
	if(raiz->hijo_izq!=NULL){
		clear(raiz->hijo_izq);
	}
	if(raiz->hijo_der!=NULL){
		clear(raiz->hijo_der);
	}

	free(raiz);
}

void print_inorden(nodo_t *raiz){
	
	if(raiz->hijo_izq!=NULL){
		print_inorden(raiz->hijo_izq);
		
	}printf("%d ", raiz->dato);
	if(raiz->hijo_der!=NULL){
		print_inorden(raiz->hijo_der);
	}
}

void print_preorden(nodo_t *raiz){
	
	printf("%d ", raiz->dato);
	if(raiz->hijo_izq!=NULL){
		print_preorden(raiz->hijo_izq);
		
	}if(raiz->hijo_der!=NULL){
		print_preorden(raiz->hijo_der);
	}
}

void print_postorden(nodo_t *raiz){
	
	if(raiz->hijo_izq!=NULL){
		print_postorden(raiz->hijo_izq);
		
	}if(raiz->hijo_der!=NULL){
		print_postorden(raiz->hijo_der);
	}
	printf("%d ", raiz->dato);
}

nodo_t *search(nodo_t *raiz, int value){
	if(raiz == NULL || raiz->dato == value){
		return raiz;
	}else if(value < raiz->dato){
		return search(raiz->hijo_izq, value);
	}else if(value > raiz->dato){
		return search(raiz->hijo_der, value);
	}
	printf("no entro a ningun caso\n");
	return NULL;
}

nodo_t *padre(nodo_t *raiz, int value){
	if(raiz == NULL || raiz->hijo_izq->dato == value || raiz->hijo_der->dato == value){
		return raiz;
	}else if(value < raiz->dato){
		return padre(raiz->hijo_izq, value);
	}else if(value > raiz->dato){
		return padre(raiz->hijo_der, value);
	}
	printf("no entro a ningun caso\n");
	return NULL;
}

int size(nodo_t *raiz){
	
	if(raiz==NULL){
		return 0;
	}
	return 1 + size(raiz->hijo_izq) + size(raiz->hijo_der);	

}


int delete(nodo_t *raiz, int value){
	
	nodo_t *find = search(raiz, value);
	nodo_t *father = padre(raiz,value);

	if(find==NULL){
		printf("El nodo no existe\n");
		return -1;
	}else{
		if(find->hijo_izq == NULL && find->hijo_der==NULL){
			printf("hijo: %d father: %d\n", find->dato, father->dato);  
			if(father->hijo_izq == find){
				father->hijo_izq = NULL;
			}else if(father->hijo_der == find){
				father->hijo_der = NULL;
			}free(find);
		}
	}
	return 1;
}

int main(int argc,char **argv){

	nodo_t *root = NULL;

	insert(&root, 19);
	insert(&root, 6);
	insert(&root, 30);
	insert(&root, 2);
	insert(&root, 15);
	insert(&root, 21);
	insert(&root, 36);
	insert(&root, 7);
	insert(&root, 17);
	insert(&root, 27);

	printf("lista Pre orden: "); print_preorden(root);	printf("\n");
	printf("lista In orden: "); print_inorden(root);      printf("\n");
	printf("lista Post orden: "); print_postorden(root);  printf("\n");
	
	nodo_t *find = NULL;
	find = search(root,22);
	if(find!=NULL){
		printf("valor encontrado en %p, valor : %d\n", find, find->dato); 
	}else 
		printf("el valor no se encuentra en el arbol\n");


	printf("el tamaño del arbol es %d\n", size(root));
	
	delete(root, 17);
	delete(root, 7);

	printf("lista Pre orden: "); print_preorden(root);	printf("\n");
	printf("lista In orden: "); print_inorden(root);      printf("\n");
	printf("lista Post orden: "); print_postorden(root);  printf("\n");
	
	clear(root);	

	return 0;
}
