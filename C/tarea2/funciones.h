#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int i,j; //for
float CI_I, CI_F, tiempo_I;
float CM_I, CM_F, tiempo_M;
float CR_I, CR_F, tiempo_R;

void InsertSort(int arr[], int n); //O(n²)

void Merge(int arr[], int l, int m, int r); 
void MergeSort(int arr[], int l, int r); //O(nlogn)

int Maximo(int arr[], int n);
void countSort(int arr[], int n, int exp);
void Radixsort(int arr[], int n); //O(d x n)
