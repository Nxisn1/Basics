#include<stdio.h>


int main(){

	int a, b;
	
	printf("Ingrese el primer valor: "); scanf("%d", &a);
	printf("Ingrese el segundo valor: "); scanf("%d", &b);

	if(a==0 || b==0){
		printf("no wei po como poni 0");
	}else if (a<b){
		if (b%a == 0){
			printf("%d es divisor de %d",a, b);
		}else{printf("%d no es divisor de %d", a,b);}
	}else if (a>b){
		if (a%b == 0){
			printf("%d es divisor de %d",b, a);
		}else{printf("%d no es divisor de %d", b,a);}
	}else if(a==b){
		printf("Si es divisor"); }

	return 0;
}
