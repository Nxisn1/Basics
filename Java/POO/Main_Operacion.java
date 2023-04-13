package src;

import javax.swing.*;

public class Main_Operacion {
    public static void main(String[] args){
        int n1 = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        int n2 = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));

        src.Operacion op = new src.Operacion();

        System.out.println("La suma es: "+op.sumar(n1, n2));
        System.out.println("La resta es: "+op.restar(n1, n2));
        System.out.println("La división es: "+op.multiplicar(n1, n2));
        System.out.println("La multiplicación es: "+op.dividir(n1, n2));

        

    }
}
