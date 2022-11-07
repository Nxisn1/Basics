#include "t1.h"


int main(){

	char is[100] = " hola como estas yo muy bien ";

	for(int i=0;i<strlen(is);i++){
		if(is[i]!=' '){
			printf("%c", is[i]);
		}
		
	}

	printf("%s\n", is);





	return 0;
}