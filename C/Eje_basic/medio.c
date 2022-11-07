#include<stdio.h>



int main(){
	
	int p1,p2,p3;
	float media;

	printf("Introduzca el precio del producto en el local 1, en pesos: "); scanf("%d", &p1);
	printf("Introduzca el precio del producto en el local 2, en pesos: "); scanf("%d", &p2);
	printf("Introduzca el precio del producto en el local 3, en pesos: "); scanf("%d", &p3);
	
	media = (p1+p2+p3)/3;

	printf("El precio medio del producto es: %.1f Pesos \n", media);


	return 0;
}
