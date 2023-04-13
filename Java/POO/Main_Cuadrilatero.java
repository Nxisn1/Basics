import javax.swing.*;

public class Main_Cuadrilatero {
    public static void main(String[] args){
        Cuadrilatero c1;
        float lado1, lado2;

        lado1 = Float.parseFloat(JOptionPane.showInputDialog("Digita el lado 1: "));
        lado2 = Float.parseFloat(JOptionPane.showInputDialog("Digita el lado 2: "));

        if(lado1 == lado2){
            c1 = new Cuadrilatero(lado1);
        }else{
            c1 = new Cuadrilatero(lado1, lado2);
        }

        System.out.println("El perímetro es: "+ c1.getPetimetro());
        System.out.println("El área es: "+ c1.getArea());


    }
}
