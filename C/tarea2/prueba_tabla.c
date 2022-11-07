#include"funciones.h"


int main(){
	int i, j=0; 
	long int n=1000;

	FILE *anal = fopen("prueba_anal.txt", "w");

	for(i=0; i<4; i++){
		int *datos1 = (int*)malloc(n * sizeof(int));
		int *datos2 = (int*)malloc(n * sizeof(int));
		int *datos3 = (int*)malloc(n * sizeof(int));
		for(j; j<n; j++){
			datos1[j] = rand();
			datos2[j] = datos1[j];
			datos3[j] = datos1[j];
		}

		CI_I = clock();
	   	//InsertSort(datos1, n);
	    CI_F = clock();

	    CM_I = clock();
	    MergeSort(datos2, 0, n-1);
	    CM_F = clock();

	    CR_I = clock();
	    Radixsort(datos3, n);
	    CR_F = clock();

	    tiempo_I = (CI_F - CI_I)/CLOCKS_PER_SEC;
    	tiempo_M = (CM_F - CM_I)/CLOCKS_PER_SEC;
    	tiempo_R = (CR_F - CR_I)/CLOCKS_PER_SEC;


	    fprintf(anal,"Tiempo InsertSort con %ld datos: ", n); fprintf(anal, "%.1f\n", tiempo_I);
	    fprintf(anal,"Tiempo MergeSort con %ld datos: ", n); fprintf(anal, "%.6f\n", tiempo_M);
	    fprintf(anal,"Tiempo RadixSort con %ld datos: ", n); fprintf(anal, "%.6f\n", tiempo_R);
	    fprintf(anal, "\n");

	    free(datos1);
	    free(datos2);
	    free(datos3);

	    n = n*10;
	}
	fclose(anal);



return 0;
}