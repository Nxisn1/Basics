/* Matriz Simétrica:
        1) Matriz cuadrada (nFilas == nColumnas).
        2) Se obtiene la misma matriz al cambiar sus filas por columnas.
 */

import javax.swing.JOptionPane;
import java.util.Scanner;

public class matriz_simetrica {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int matriz[][], nFilas, nCol;
        boolean simetrica = true;

        nFilas = Integer.parseInt(JOptionPane.showInputDialog("Digita el número de filas: "));
        nCol = Integer.parseInt(JOptionPane.showInputDialog("Digita el número de columas: "));

        matriz = new int[nFilas][nCol];

        System.out.println("Digita una matriz: ");
        for(int i=0; i<nFilas; i++){
            for(int j=0; j<nCol; j++){
                System.out.println("Matriz ["+i+"]["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }


        if(nFilas == nCol){
            int i, j;
            i=0;
            while(i<nFilas && simetrica==true){
                j=0;
                while(j<i && simetrica==true){
                    if(matriz[i][j] != matriz[j][i]){
                        simetrica = false;
                    }
                    j++;
                }
                i++;
            }

            if(simetrica==true){
                JOptionPane.showMessageDialog(null, "la matriz es siméttrica.");
            }else{
                JOptionPane.showMessageDialog(null, "La matriz no es simétrica");
            }
        }else{
            JOptionPane.showMessageDialog(null, "La matriz no es simétrica");
        }

    }

}
