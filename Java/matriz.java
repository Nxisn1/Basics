import javax.swing.*;
import java.util.Scanner;

/* las matrices se cuentan igual que los arreglos, empiezan de 0
una matriz es un array de array's

*/
import java.util.Scanner;
import javax.swing.JOptionPane;

public class matriz {
    public static void main(String[] args){

        Scanner entrada = new Scanner(System.in);
        int matriz[][], nFilas, nCol;

        nFilas = Integer.parseInt(JOptionPane.showInputDialog("Digita el número de filas: "));
        nCol = Integer.parseInt(JOptionPane.showInputDialog("Digita el número de columnas: "));

        matriz = new int[nFilas][nCol];

        System.out.println("Digite la matriz: ");
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

    }
}
