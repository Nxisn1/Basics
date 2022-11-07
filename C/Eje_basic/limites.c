#include<stdio.h>


int main(){	
	float a, lim_i=100, lim_s=200;
	printf("Ingrese un número real: "); scanf("%f", &a);
	if (a >= lim_i){
		if (a <= lim_s){
		printf("%.2f está entre los límites", a);
		}else{
			printf("%.2f No está entre los límites", a);}	
	}else{
		printf("%.2f No está entre los límites", a);	
	}
	return 0;
}
