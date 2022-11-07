#include<stdio.h>

int main(){

	int Tu, To, Cap_tu, Cap_to, Total_com;

	printf("Ingrese la cantidad de vehiculos de turismo: "); scanf("%d",&Tu);
	printf("Ingrese la cantidad de vehiculos todoterreno: "); scanf("%d",&To);
	printf("Ingrese la capacidad de combustible de los vehiculos de turismo litros: "); scanf("%d",&Cap_tu);
	printf("Ingrese la capacidad de combustible de los vehiculos todoterreno en litros: "); scanf("%d",&Cap_to);
	
	Total_com = (Tu*Cap_tu)+(To*Cap_to);

	printf("El total de combustible que se necesita es: %d [L]\n", Total_com);

	return 0;
}
