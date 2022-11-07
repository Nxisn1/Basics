#include"funciones.h"


int main(int argc, char **argv){

    if(argc!=2){printf("Número de parámetros incorrecto\n"); exit(-1);}

    int size = 1920*1080; //cantidad de datos 
    int *datos_I = (int*)malloc(size * sizeof(int));
    int *datos_M = (int*)malloc(size * sizeof(int));
    int *datos_R = (int*)malloc(size * sizeof(int));
    
    FILE *fichero = fopen(argv[1], "rb"); //abrirlo y leerlo en binario
        if(fichero==NULL){ //si hay un error con abrir el archivo
            printf("Problema con archivo\n");
            exit(-1);
        }

    fseek(fichero, 0, SEEK_SET); //para empezar desde le principio
    int num_I = fread(datos_I, sizeof(int), size, fichero);
    fseek(fichero, 0, SEEK_SET);
    int num_M = fread(datos_M, sizeof(int), size, fichero);
    fseek(fichero, 0, SEEK_SET);
    int num_R = fread(datos_R, sizeof(int), size, fichero);
    if ((num_I+num_M+num_R) == 3*size) printf("todo ha salido bien.\n");
    else printf("Algo anda mal, no se tomaron todos los datos.\n");
    fclose(fichero);

    CI_I = clock();
    //InsertSort(datos_I, size);
    CI_F = clock();

    CM_I = clock();
    MergeSort(datos_M, 0, size-1);
    CM_F = clock();

    CR_I = clock();
    Radixsort(datos_R, size);
    CR_F = clock();

    tiempo_I = (CI_F - CI_I)/CLOCKS_PER_SEC;
    tiempo_M = (CM_F - CM_I)/CLOCKS_PER_SEC;
    tiempo_R = (CR_F - CR_I)/CLOCKS_PER_SEC;

    FILE *slda_I = fopen("salida_Insert.pbm", "w");
    FILE *slda_M = fopen("salida_Merge.pbm", "w");
    FILE *slda_R = fopen("salida_Radix.pbm", "w");

    fprintf(slda_I, "%s\n","P1"); //datos del pbm de Insert
    fprintf(slda_I, "%s\n","1920 1080");
    fprintf(slda_M, "%s\n","P1"); //datos del pbm de MERGE
    fprintf(slda_M, "%s\n","1920 1080");
    fprintf(slda_R, "%s\n","P1"); //datos del pbm de RADIX
    fprintf(slda_R, "%s\n","1920 1080");

    for(i=1;i<=size;i++){  //escribir los datos en el pbm de salida Insert
        fprintf(slda_I, "%d", datos_I[i]%2);
    }  
    for(i=1;i<=size;i++){  //merge
        fprintf(slda_M, "%d", datos_M[i]%2);
    }
    for(i=1;i<=size;i++){  //radix
        fprintf(slda_R, "%d", datos_R[i]%2);
    }   

    fclose(slda_I);
    fclose(slda_M);
    fclose(slda_R);

    free(datos_I); 
    free(datos_M); 
    free(datos_R);   

    FILE *analisis = fopen("analisis.txt", "w");

    fprintf(analisis, "%s","Cantidad de instrucciones por segundo: "); fprintf(analisis, "%ld\n\n", CLOCKS_PER_SEC); 

    fprintf(analisis, "%s\n","InsertSort O(n²)");
    fprintf(analisis, "%s","Tiempo que tarda InsertSort para ordenar el arreglo de la imagen: "); fprintf(analisis, "%.1f", tiempo_I/60); fprintf(analisis, "%s\n", "[min]");  

    fprintf(analisis, "%s\n","MergeSort O(nlogn)");
    fprintf(analisis, "%s","Tiempo que tarda MergeSort para ordenar el arreglo de la imagen: "); fprintf(analisis, "%.3f", tiempo_M); fprintf(analisis, "%s\n", "[s]");
    
    fprintf(analisis, "%s\n","RadixSort O(n x d)");
    fprintf(analisis, "%s","Tiempo que tarda RadixSort para ordenar el arreglo de la imagen: "); fprintf(analisis, "%.3f", tiempo_R); fprintf(analisis, "%s\n", "[s]");
    fprintf(analisis, "\n");

    //analisis
    long int n=1000;//analisis
    for(i=0; i<4; i++){
        int *datos1 = (int*)malloc(n * sizeof(int));
        int *datos2 = (int*)malloc(n * sizeof(int));
        int *datos3 = (int*)malloc(n * sizeof(int));
        for(j=0; j<n; j++){
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


        fprintf(analisis,"Tiempo InsertSort con %ld datos: ", n); fprintf(analisis, "%.1f", tiempo_I); fprintf(analisis, "%s\n", "[s]");
        fprintf(analisis,"Tiempo MergeSort con %ld datos: ", n); fprintf(analisis, "%.6f", tiempo_M); fprintf(analisis, "%s\n", "[s]");
        fprintf(analisis,"Tiempo RadixSort con %ld datos: ", n); fprintf(analisis, "%.6f", tiempo_R); fprintf(analisis, "%s\n", "[s]");
        fprintf(analisis, "\n");

        free(datos1);
        free(datos2);
        free(datos3);

        n = n*10;
    }


    fclose(analisis);

    return 0;
}