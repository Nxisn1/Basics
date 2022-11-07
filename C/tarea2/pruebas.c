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


int main(){


	int *arr = (int*)malloc(10*sizeof(int));

	//int arr[10] = {3,7,8,4,5,6,10,2,1,9};
	for(int i=0;i<10;i++){ //llenar el arreglo
		arr[i] = rand();
	}
	for(int i=0;i<10;i++){  //printear el arreglo;
		printf("%d ", arr[i]);
	}

	printf("\n");


    int time_inicial = clock(); 

    mergeSort_G(arr, 0, 9);

	int time_final = clock(); 

	for(int i=0;i<10;i++){    //printear array ordenado de menor a mayor
		printf("%d ", arr[i]);
	}
	printf("\n");

    printf(" tiempo inicial: %d\n tiempo final: %d\n", time_inicial, time_final);


	return 0;
}

//INFO

//TIEMPO

/* time = clock(); printf("%d\n", time); PA VER LE TIEMPO*/


//PARAMETROS
//insertionSort(arr,10); 
//quickSort(arr,0, 9); 
//radixsort(arr, 10);
//mergeSort(arr, 0, 9);