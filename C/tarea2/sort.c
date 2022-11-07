#include "funciones.h"

void InsertSort(int arr[], int n){ 
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


void Merge(int arr[], int l, int m, int r){
 
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
    }  //O(nlogn)
}
void MergeSort(int arr[], int l, int r){
    if(l<r){
        int m = l + (r-l)/2;

        MergeSort(arr, l, m);
        MergeSort(arr, m+1,r);

        Merge(arr, l, m, r);
    }  
}


int Maximo(int arr[], int n){
    int max = arr[0];
    int i;
    for (i = 1; i < n; i++)
        if (arr[i] > max)
            max = arr[i];
    return max; //número máximo
}
void countSort(int arr[], int n, int exp){
    int salida[n];
    int i, count[10] = {0};
 
    for (i = 0; i < n; i++)
        count[(arr[i] / exp) % 10]++;
 
    for (i = 1; i < 10; i++)
        count[i] += count[i - 1];
 
    for (i = n - 1; i >= 0; i--) { //meterlos a salida
        salida[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }

    for (i = 0; i < n; i++)
        arr[i] = salida[i];
}
void Radixsort(int arr[], int n){
    int m = Maximo(arr, n);
    int exp;
    for (exp = 1; m / exp > 0; exp *= 10)
        countSort(arr, n, exp); 
}
