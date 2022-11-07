#include<stdio.h>
#include<stdlib.h>
#include "t1.h"

int lineas=0;

int  main(){

	fichero = fopen("seq_test.txt", "rt"); 
	fscanf(fichero, "%*s\n"); //saltarse la primera línea
	int w[10];


	while(true){   //CONTAR LINEAR

		char aux  = fgetc(fichero);
		if(aux == '\n'){
			lineas++;
		}if(aux == EOF){
			fichero = fopen("seq_test.txt", "rt"); 
			//printf("%d\n",lineas);
			break;
		}
	}

	/*fscanf(fichero, "%*s\n"); //saltarse la primera línea
    
    for(int i=0;i<lineas;i++){ //recorrer linea por linea el arch
    	fgets(w, 100, fichero);	
   	 	printf("%s\n", w);
   	 	
	}
	fclose(fichero);
*/

	fichero = fopen("seq_test.txt", "rt"); 
	fscanf(fichero, "%*s\n"); //saltarse la primera línea
	for(int i=0;i<lineas-1;i++){ //recorrer ID por ID el arch de personas

		fscanf(fichero, "%d\n",w);
		printf("%d\n", *w);

		for(int j=0;j<6;j++){
			fscanf(fichero, "%*s\n");
		}
	}

	fclose(fichero);

	return 0;
}