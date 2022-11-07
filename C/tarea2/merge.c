#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>    


void merge_G(int arr[], int l, int m, int r){
 
    int n1, n2, i, j, k;

    n1 = m - l + 1;
    n2 = r - m;

    int L[n1], R[n2];

    for(i=0;i<n1;i++)
        L[i]=arr[l+i];
    for(j=0;j<n2;j++)
        R[j]=arr[m+1+j];
    

    i=0;j=0;k=l;
    while(i<n1 && j<n2){
        if(L[i] <= R[j]){
            arr[k] = L[i]; i++;
        }else{
            arr[k] = R[j]; j++;
        }
        k++;
    }

    while(i<n1){
        arr[k] = L[i]; i++; k++;
    }
    while(j<n2){
        arr[k] = R[j]; j++; k++;
    }
}
void mergeSort_G(int arr[], int l, int r){
    if(l<r){
        int m = l + (r-l)/2;

        mergeSort_G(arr, l, m);
        mergeSort_G(arr, m+1,r);

        merge_G(arr, l, m, r);
    }
}

void merge(int A[ ] , int start, int mid, int end){
     //stores the starting position of both parts in temporary variables.
    int p = start ,q = mid+1;

    int Arr[end-start+1], k=0;

    for(int i = start ;i <= end ;i++) {
        if(p > mid)      //checks if first part comes to an end or not .
            Arr[ k++ ] = A[ q++] ;

        else if ( q > end)   //checks if second part comes to an end or not
            Arr[ k++ ] = A[ p++ ];

        else if( A[ p ] < A[ q ])     //checks which part has smaller element.
            Arr[ k++ ] = A[ p++ ];

        else
            Arr[ k++ ] = A[ q++];
    }
    for (int p=0 ; p< k ;p ++) {
        /* Now the real array has elements in sorted manner including both 
        parts.*/
        A[ start++ ] = Arr[ p ] ;                          
    }
}
void mergeSort(int A[ ] , int start , int end ){
      if( start < end ) {
           int mid = (start + end ) / 2 ;           // defines the current array in 2 parts .
           mergeSort (A, start , mid ) ;                 // sort the 1st part of array .
           mergeSort (A,mid+1 , end ) ;              // sort the 2nd part of array.

         // merge the both parts by comparing elements of both the parts.
          merge(A,start , mid , end );   
   }                    
}

void merge_stack(int a[],int beg,int mid,int end){
    int i=beg,j=mid+1,index=beg,temp[100],k;
    while((i<=mid) && (j<=end))
    {
        if(a[i]<a[j])
        {
            temp[index]=a[i];
            i=i+1;
        }
        else
        {
            temp[index]=a[j];
            j++;
        }
        index++;
    }
    if(i>mid)
    {
        while(j<=end)
        {
            temp[index]=a[j];
            j++;
            index++;
        }
    }
    else
    {
        while(i<=mid)
        {
            temp[index]=a[i];
            i++;
            index++;
        }
    }
    for(k=beg;k<index;k++)
    {
        a[k]=temp[k];
    }
}
void mergesort_stack(int a[],int beg,int end){
    int mid;
    if(beg<end)
        mid = (beg+end)/2;
        mergesort_stack(a,beg,mid);
        mergesort_stack(a,mid+1,end);
        merge_stack(a,beg,mid,end);
}

int main(int argc, char **argv){

    if(argc!=2){printf("Número de parámetros incorrecto\n"); return .1;}

    int size = 1920*1080; //cantidad de datos 
    //int datos[size];
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

    mergeSort_G(datos, 0, size-1);

    t_final = clock();

    for(int j=0;j<size;j++){
        printf("%d\n", datos[j]);
    }

    printf(" Tiempo inical: %d\n Tiempo final: %d\n", t_inicial, t_final);
    
    return 0;
};