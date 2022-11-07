#include<stdio.h>
#define PI 3.141593

int main(){

	float D, H, R, V;

	printf("Introduzca el diámetro, en metros: "); scanf("%f", &D);
	printf("Introduzca la altura, en metros: "); scanf("%f", &H);    //acuerdate de los & wn
	R = D/2;
	V = PI*(R*R)*H;

	printf("El volumen del cilindro es: %.2f metros cúbicos \n" , V); //el .2 es para la precisión (2 decimales)
		
	return 0;
};
