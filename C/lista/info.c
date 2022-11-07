//LISTA SIMPLE ENLAZADA

//dos tipos para hacer listas enlazadas 

struct nodo{
	int dato; 
	struct nodo *sgte;
};


mejor:
typedef struct le_nodo{
	float datos[20];
	struct le_nodo *sgte;
} nodo_t; 


//funcion para primer nodo
void first_node(nodo_t **cabeza, int dato){

	nodo_t *nuevo = malloc(sizeof(nodo_t)); //crea el nodo
	nuevo -> dato = dato;	//asigna dato
	nuevo -> sgte = NULL;   // siguiente apunta a NULL
	*cabeza = nuevo;	// inicio apunta a nuevo
}


//funcion para agregar al inicio
void add_first(nodo_t **cabeza, int dato){

	nodo_t *nuevo = malloc(sizeof(nodo_t)); //crea nodo
	nuevo->dato = dato;    //asigna dato
	nuevo->sgte = *cabeza; //siguiente apunta a inicio
	*cabeza = nuevo;       //inicio apunta a nuevo
}



//funcion agregar en pos
void add_node_pos(node_t *cabeza, int dato, int pos){

	nodo_t *nuevo = malloc(sizeof(nodo_t)); //crear nodo
	nuevo -> dato = dato; //asigna dato

	int cont; //para ver en la posicion q vamos 
	noto_t *recorredor = cabeza; //ptr q recorre la lista

	for (cont=0; cont<pos-1; cont++){   //pos-1 para encontrar el anterior al donde queremos poner el nodo
		recorredor = recorredor->sgte; //avanza al sig nodo
	}//al finalizar el for, tenemos el nodo previo identidficado

	nuevo->sgte = recorredor->sgte;  //cambio de punteros
	recorredor->sgte = nuevo; //el orden importa, Memory Leak!
}

//funcion para añadir al final
void add_node_final(node_t *cabeza, int dato()){
		nodo_t *nuevo = malloc(sizeof(nodo_t)); //crea nodo
		nuevo->dato = dato; //asigna dato

		nodo_t *recorredor = cabeza;  //ptr q recorre la lista
		while (recorredor->sgte !=NULL){
			recorredor = recorredor->sgte;  //avanzamos hasta llegar al final
		}
		
		nuevo->sgte = recorredor->stge; //cambio de punteros
		recorredor->sgte = nuevo;   //el orden importa, Memory leak

}
	


//funcion q combina las 4 
void add_node_pos(nodo_t **cabeza, int dato, int pos){
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



















