#include<stdio.h>


int main(){

	printf("esto para mostrar lo q sea\n"); //con salto de linea

	int A,B;
	char nom[10];  //lo mismo q c++

	printf("Ingrese valor de A: "); //equivalente al cout
	scanf("%d", &A); /*los %d son para indicarle q son enteros. para tipo de dato es necesario 
				  poner su identificador, esto es de la libreria stdio.h
				  scanf equivalente a cin*/
	printf("Ingrese valor de B: ");
	scanf("%d", &B); //con el scanf no se te olvide ponerle el & a la variable para indicar q se guarde donde debe, o sino error


	printf("El valor de A es: %d y el valor de B: %d\n", A,B); //aqui tmb debemos poner los identificadores
	 	

	A = (A>5) ? 2*A : --A; //tmb sirve el ++ y --
	printf("%d\n",A);

	return 0;

}
