#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>    /* time = clock(); printf("%d\n", time); PA VER LE TIEMPO*/


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

    int datos[1920*1080]; //memoria fija no dinamica ojo
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

    //insertionSort(datos, size);
    //quickSort(datos, 0, size-1);
    //radixsort(datos, size-1);
    //mergeSort_G(datos, 0, size);

    t_final = clock();

    for(int j=0;j<size;j++){
        printf("%d\n", datos[j]);
    }

    printf(" Tiempo inical: %d\n Tiempo final: %d\n", t_inicial, t_final);
    
    return 0;
};

