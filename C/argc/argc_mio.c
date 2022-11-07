#include<stdio.h>

int main(int argc, char **argv){

	int a = (int)&argv[1];
	printf("eso: %d\n", a*2);
	return 0;
}
