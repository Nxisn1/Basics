#include "t1.h"
#include<stdlib.h>
#include<stdio.h>
#include<sys/stat.h>

int lines(const char *arch){
	int lineas=0;

	FILE *fichero = fopen(arch, "rb"); 
 	if(fichero==NULL){
 		printf("algo anda mal\n");
 		return -1;
 	}

	
	fscanf(fichero, "%*s\n");
	for(;;){   //CONTAR LINEAR
		char aux  = fgetc(fichero);
		if(aux == '\n'){
			lineas++;
		}if(aux == EOF){
			fichero = fopen(arch, "rt");
			return lineas;
		}
	}
	fclose(fichero);
}
void *nom_V(const char *arch){

 	char w[100];

 	FILE *fichero = fopen(arch, "rb"); 
 	if(fichero==NULL){
 		printf(" problema con archivo\n");
 		exit(-1);

 	}
 	
	
	int line = lines(arch);
	fscanf(fichero, "%*s\n"); //saltarse la primera línea
	for(int i=0;i<line;i++){ //recorrer ID por ID el arch
		fscanf(fichero, "%s\n",w);
		printf("%s\n", w);
		for(int j=0;j<3;j++){
			fscanf(fichero, "%s\n",w);
		}
	}
	fclose(fichero);
}
int *IDs(const char *arch){

	fichero = fopen(arch, "rt"); 
	int line = lines(arch);
	int w[10];
	fscanf(fichero, "%*s\n"); //saltarse la primera línea
	for(int i=0;i<line-1;i++){ //recorrer ID por ID el arch de personas

		fscanf(fichero, "%d\n",w);
		printf("%d\n", *w);

		for(int j=0;j<6;j++){
			fscanf(fichero, "%*s\n");
		}
	}
	fclose(fichero);
}
void *linea_linea(const char *arch){
	char w[100];

	FILE *fichero = fopen(arch, "rb"); 
	if(fichero==NULL){
 		printf(" problema con archivo\n");
 		exit(-1);

 	}
	int lineas = lines(arch);
	fscanf(fichero, "%*s\n"); //saltarse la primera línea
    
    for(int i=0;i<lineas;i++){ //recorrer linea por linea el arch
    	fscanf(fichero, "%*s\n"); //salta la ID
    	fgets(w, 100, fichero);	
   	 	printf("%s\n", w);
	}
	fclose(fichero);
}
/*
void list_V(variante **head){

	FILE *fichero = fopen("var.txt", "rb"); 
	int line=lines("var.txt");
	for(int  i=0;i<line;i++)
		variante *nuevo = malloc(sizeof(variante)); 
		nuevo->nom = leer_ID("var.txt");

		if(nuevo==NULL){ //falla malloc
			printf("falla de malloc\n");
			exit (-1);
		}

		if(*head==NULL){
			nuevo->sgte = *head;
			*head = nuevo;
	
		}else{

			variante *rec = *head;
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
*/

void list_P(paciente **head, int ID, int pos){

	paciente *nuevo = malloc(sizeof(paciente));
	nuevo->id = ID;

	if(nuevo==NULL){ 
		printf("falla de malloc\n");
		exit (-1);
	}

	if(*head==NULL || pos==0){
		nuevo->sgte = *head;
		*head = nuevo;
	
	}else{

		paciente *rec = *head;
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


void print_list(paciente *head){

	paciente *rec = head;
	printf("[");
	while(rec!=NULL){
		printf("%d ", rec->id);
		rec = rec->sgte;
	}
	printf("]\n"); 
}





int main(){

	//printf("%d\n", lines("var.txt"));
	//leer_ID("var.txt");
	//linea_linea("var.txt");

	paciente *inicio = NULL;
	int li = lines("seq_test.txt");

	for(int i=0;i<li;i++){
		printf("%d\n",*IDs("seq_test"));
		//list_P(&inicio, IDs("seq_test"), i);
	}

	print_list(inicio);


	return 0;
}