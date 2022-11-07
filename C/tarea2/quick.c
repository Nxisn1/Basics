#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>    


int random_partition(int arr[], int inicio, int fin){
    int index = rand() %(fin+1);
    int pivote = arr[index];
    int i = inicio-1, j = fin + 1;

    while(1){
        do{
            i++;
        }while(arr[i] < pivote);
        do{
            j--;
        }while(arr[j] > pivote);

        if(i >= j)
            return j;

        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
void  quickSort(int arr[], int inicio, int fin){ //O(nlogn)
    if(inicio < fin){

        int corte = random_partition(arr, inicio, fin);

        quickSort(arr, inicio, corte);
        quickSort(arr, corte + 1, fin);

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