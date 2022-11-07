// Codigo by R-I-R
// Al ejecutar se pasa como parametro el nombre del archivo de la imagen pbm

#include <bits/stdc++.h>

int main(int argc, char **argv){
	FILE *binario, *pbm;

	pbm = fopen(argv[1],"r");

	char s[71];
	fscanf(pbm,"%[^\n]s ",s);
	if(s[0] != 'P' || s[1] != '1') exit(1);

	int ancho,alto,totald;
	while(fscanf(pbm," %[^\n]s ",s),s[0] == '#');
	sscanf(s,"%d %d",&ancho,&alto);
	totald = ancho*alto;

	printf("ancho: %d alto: %d totald:%d\n",ancho,alto,totald);

	int *data = (int*)malloc(sizeof(int)*totald);

	int count = 0;
	char tmp[71];

	for(int a = 0; a < totald; a++){
		while(fscanf(pbm," %1[10#]s ",tmp),tmp[0] == '#') fscanf(pbm,"%*[^\n]s");
		//printf("%s\n",tmp);
		data[a]=(tmp[0]=='1'?count+1:count);
		count += 2;
	}
	
	fclose(pbm);

	std::random_shuffle(data,data+(ancho*alto-1));

	binario = fopen((std::string(argv[1])+".bin").c_str(),"wb");
	fwrite(data,sizeof(int),ancho*alto,binario);
	fclose(binario);

	return 0;
}