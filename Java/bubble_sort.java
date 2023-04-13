//algoritmo de ordenamiento, bubble sort

import javax.swing.*;
import java.util.Scanner;

public class bubble_sort {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int arreglo[], nElementos, aux;

        nElementos = Integer.parseInt(JOptionPane.showInputDialog("Cantidad del arreglo"));

        arreglo = new int[nElementos];

        for(int i=0; i<nElementos; i++){
            System.out.println((i+1)+". Digíta un número");
            arreglo[i] = entrada.nextInt();
        }

        //Método burbuja
        for(int i=0; i<(nElementos-1); i++){ //si el arreglo tiene 5 números, no es necesario que lo recorra 5 veces, con 4 basta
            for(int j=0; j<(nElementos-1); j++){ //para ordenar
                if(arreglo[j] > arreglo[j+1]){ //Si numeroActual > numeroSiguiente
                    aux = arreglo[j];
                    arreglo[j] = arreglo[j+1];
                    arreglo[j+1] = aux;
                }
            }
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