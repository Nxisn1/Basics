//algoritmo de ordenamiento, Insert Sort O(n^2).

import javax.swing.*;
import java.util.Scanner;

public class insert_sort {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int arreglo[], nElementos, pos, aux;


        nElementos = Integer.parseInt(JOptionPane.showInputDialog("Cantidad del arreglo"));
        arreglo = new int[nElementos];

        for(int i=0; i<nElementos; i++){
            System.out.println((i+1)+". Digíta un número");
            arreglo[i] = entrada.nextInt();
        }

        //Insert Sort
        for(int i=0; i<nElementos; i++){
            pos = i;
            aux = arreglo[i];
            while((pos>0) && (arreglo[pos-1] > aux)){
                arreglo[pos] = arreglo[pos-1];
                pos--;
            }
            arreglo[pos] = aux;
        }

        //Mostrar el arreglo ordenado de forma creciente
        System.out.println("\nArreglo ordenado de forma creciente: ");
        for(int i=0; i<nElementos; i++){
            System.out.print(arreglo[i]+" - "); //el último queda con un guión (-) (Estético nomás)
        }


        //Mostrar el arreglo ordenado de forma decreciente
        System.out.println("\nArreglo ordenado de forma decreciente: ");
        for(int i=(nElementos-1); i>=0; i--){
            System.out.print(arreglo[i]+" - "); //el último queda con un guión (-) (Estético nomás)
        }
    }
}

