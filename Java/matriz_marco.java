/* matriz 5x5 de 1 y 0, los bordes son 1 formando un marco

1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1

cuando se crea una matriz en java automaticamente es una matriz de puros 0
 */

public class matriz_marco {
    public static void main(String[] args){
        int matriz[][] = new int[5][5];

        //Rellenando la matriz
        for(int i=0; i<5; i++){
            for(int j=0; j<5; j++){
                if(i==0 || i==4){ //delimita las columnas
                    matriz[i][j] = 1;
                }else if(j==0 || j==4){
                    matriz[i][j] = 1;
                }else{
                    matriz[i][j] = 0; //Esto no es necesario por lo de arriba, pero pa q se vea bonito
                }
            }
        }


        System.out.println("\nLa matriz es: ");
        for(int i=0; i<5; i++) { //número de filas
            for (int j = 0; j<5; j++) { //número de columnas
                System.out.print(matriz[i][j]+" ");
            }
            System.out.println("");
        }
    }
}
