#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>    

int getMax(int arr[], int n){
    int mx = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > mx)
            mx = arr[i];
    return mx;
}
void countSort(int arr[], int n, int exp){
    int output[n]; // output array
    int i, count[10] = { 0 };
 
    // Store count of occurrences in count[]
    for (i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;
 
    // Change count[i] so that count[i] now contains actual
    //  position of this digit in output[]
    for (i = 1; i < 10; i++)
        count[i] += count[i - 1];
 
    // Build the output array
    for (i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }
 
    // Copy the output array to arr[], so that arr[] now
    // contains sorted numbers according to current digit
    for (i = 0; i < n; i++)
        arr[i] = output[i];
}
void radixsort(int arr[], int n){
    // Find the maximum number to know number of digits
    int m = getMax(arr, n);
 
    // Do counting sort for every digit. Note that instead
    // of passing digit number, exp is passed. exp is 10^i
    // where i is current digit number
    for (int exp = 1; m / exp > 0; exp *= 10)
        countSort(arr, n, exp); //O(d x n)
}


int main(int argc, char **argv){

    if(argc!=2){printf("Número de parámetros incorrecto\n"); return .1;}

    int size = 1920*1080; //cantidad de datos 
    int *datos = (int*)malloc(size * sizeof(int));
    int t_inicial, t_final;
    


    FILE *fichero = fopen(argv[1], "rb"); //abrirlo y lerrlo en binario
        if(fichero==NULL){ //si hay un erro con abrir el archivo
            printf(" problema con archivo\n");
            exit(-1);
        }
    fseek(fichero, 0, SEEK_SET); //para que empieze desde le principio
    
    int num = fread(datos, sizeof(int), size, fichero);
    if (num == size) printf("todo ha salido bien.\n");
    else printf("Algo anda mal, no se tomaron todos los datos.\n");
    fclose(fichero);

    t_inicial = clock(); 

    radixsort(datos, size);

    t_final = clock();

    for(int j=0;j<size;j++){
        printf("%d\n", datos[j]);
    }

    printf(" Tiempo inical: %d\n Tiempo final: %d\n", t_inicial, t_final);
    
    return 0;
};