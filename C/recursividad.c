#include<stdio.h>

int fact(int valor){

	if(valor> 1){
		return valor*fact(valor-1);
	}else{
		return 1;
	};
}


int main(){

	int a;
	printf("el fact de : ");
	scanf("%d",&a); 
	printf("El factorial es: %d\n", fact(a));

	return 0;
}
