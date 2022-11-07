#include"funciones.h"


int main(){

	int *datos1 = (int*)malloc(10 * sizeof(int));

	for(int j=0; j<10; j++){
		
		datos1[j] = rand();
		}
	
	free(datos1);


return 0;
}