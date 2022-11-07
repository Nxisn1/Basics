#include<stdio.h>
#include"archivo1.h" //se incluyen los .h no los .c
#include"archivo2.h"
 

int main(){

	print1();
	print2();

	return 0;}


	//para compilar se pone gcc -o main Varios_archivos.c archivo1.c archivo2.c -Wall
	//los headers no se compilan (se compilan al compilar los .c)
	//los .c no deben estar uno dentro de los otros, la union se hace a traves de los headers
