#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>    

void insertionSort(int arr[], int n){ //O(n²)
    int i, key, j;
    for(i=1; i<n; i++){
        key = arr[i];
        j = i-1;
        while(j >= 0 && arr[j]>key){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1]  = key;
    }

}


int main(int argc, char **argv){

    if(argc!=2){printf("Número de parámetros incorrecto\n"); return .1;}

    int datos[1920*1080];
    int t_inicial, t_final;
    int size = 1920*1080; //cantidad de datos 


    FILE *fichero = fopen(argv[1], "rb"); //abrirlo y lerrlo en binario
        if(fichero==NULL){ //si hay un erro con abrir el archivo
            printf(" problema con archivo\n");
            exit(-1);
        }
    fseek(fichero, 0, SEEK_SET); //para que empieze desde le principio
    
    int num = fread(&datos, sizeof(int), size, fichero);
    if (num == size) printf("todo ha salido bien.\n");
    else printf("Algo anda mal, no se tomaron todos los datos.\n");
    fclose(fichero);

    t_inicial = clock(); 

    insertionSort(datos, size);

    t_final = clock();

    for(int j=0;j<size;j++){
        printf("%d\n", datos[j]);
    }

    printf(" Tiempo inical: %d\n Tiempo final: %d\n", t_inicial, t_final);
    
    return 0;
};