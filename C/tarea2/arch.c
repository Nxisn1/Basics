#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>


int main(){

	FILE *a = fopen("ejemplo.txt", "wt");

	//fprintf(a, "%s"," ");
	for(int i=1;i<=100;i++){
		if(i%20 != 0){
			fprintf(a, "%d", i%2);
		}else{
			fprintf(a,"%d\n", i%2);
		}

	}

	fclose(a);

	return 0;
}