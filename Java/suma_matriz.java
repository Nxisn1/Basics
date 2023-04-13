import javax.swing.*;
import java.util.Scanner;

public class suma_matriz {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int matriz[][], nFilas, nCol, sumaFilas, sumaCol;

        nFilas = Integer.parseInt(JOptionPane.showInputDialog("Digíta el número de filas: "));
        nCol = Integer.parseInt(JOptionPane.showInputDialog("Digíta el número de columas: "));
        matriz = new int[nFilas][nCol];

        System.out.println("Digita una matriz: ");
        for(int i=0; i<nFilas; i++){
            for(int j=0; j<nCol; j++){
                System.out.println("Matriz ["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }

        System.out.println("\nLa matriz es: ");
        for(int i=0; i<nFilas; i++) { //número de filas
            for (int j = 0; j<nCol; j++) { //número de columnas
                System.out.println(matriz[i][j]);
            }
            System.out.println("");
        }

        //Ahora sumamos las filas
        for(int i=0; i<nFilas; i++){
            sumaFilas = 0;
            for(int j=0; j<nCol; j++){
                sumaFilas += matriz[i][j];
            }
            System.out.print("\nLa suma de la fila["+i+"] es: "+sumaFilas);
        }
        System.out.println("");

        //por último sumamos las columnas
        for(int j=0; j<nCol; j++){
            sumaCol = 0;
            for(int i=0; i<nFilas; i++){
                sumaCol += matriz[i][j];
            }
            System.out.print("\nLa suma de la columna ["+j+"] es: "+sumaCol);
        }
        System.out.println("");
    }
}
