#include<stdio.h>
#include<stdlib.h> //en esta libreria esta 'malloc', 'free'

typedef struct nodo{    //el typedef es para 'cambiar' su nombre; en vez de poner 'struct le_nodo' se le pone 'nodo_t'
	int dato;
	struct nodo *sgte;
	struct nodo *prev;
} nodo_t;




int main(){




	return 0;
}
