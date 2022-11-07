#include "t1.h"


int main(){

	char wea[100];
	char blo1[50];
	char blo2[50];
	char blo3[50];
    FILE *fichero;

//con esto puedes leer de 4 en 4
   
    fichero = fopen("seq_test.txt", "rt"); 
    fscanf(fichero, "%*s\n"); //saltarse la primera línea
    fscanf(fichero, "%*s\n"); //salta 
    int i=0;
    fgets(wea,100, fichero);
    printf("%s\n",wea );
    

    while(i<60){
        if(wea[i]!=' '){
            printf("%c", wea[i]);

        }

        i++;

        }


printf("\n");
        char pr = '2';
        int en = pr - '0';
        printf("%d\n", en);
        
 return 0;       

    }
    