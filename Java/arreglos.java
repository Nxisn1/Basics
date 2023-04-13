import javax.swing.*;
import java.util.Scanner;

public class arreglos {
    public static void main(String[] args){

        int[] numeros = new int[3];

         numeros[0] = 7;
         numeros[1] = 10;
         numeros[2] = 13;

         int[] numeros2 = {5,7,9,10};

         for(int i=0; i<3; i++){
             System.out.println(numeros[i]);
         }

         Scanner entrada = new Scanner(System.in);
         int nElementos;
         nElementos = Integer.parseInt(JOptionPane.showInputDialog("Digita una entero: ")); //el jop te da un string, con lo primero lo pasamos a int

         char[] letras = new char[nElementos];

         System.out.println("Digíte los números de elementos del arreglo: ");
         for(int i=0; i<nElementos; i++){
             System.out.println((i+1)+". Dígite un caracter ");
             letras[i] = entrada.next().charAt(0);
         }

         System.out.println("\nLos caracteres son: ");
        for(int i=0; i<nElementos; i++){
            System.out.println(letras[i]);
        }
    }
}
