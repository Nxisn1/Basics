#include"main.h"

int main(int argc, char **argv){

	if(argc!=2){
		printf("Error, número de parámetros incorrecto, intentelo nuevamente \n");
		return .1;
	}

	le_string(argv[1]);

	return 0;
}
