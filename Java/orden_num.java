import javax.swing.*;
 //orden de mayor a menor, no sirve para números repetidos.

public class orden_num {
    public static void main(String[] args) {
        int num1, num2, num3;
        num1 = Integer.parseInt(JOptionPane.showInputDialog("Digita una entero: ")); //el jop te da un string, con lo primero lo pasamos a int
        num2 = Integer.parseInt(JOptionPane.showInputDialog("Digita una entero: ")); //el jop te da un string, con lo primero lo pasamos a int
        num3 = Integer.parseInt(JOptionPane.showInputDialog("Digita una entero: ")); //el jop te da un string, con lo primero lo pasamos a int

        if((num1>num2) && (num2>num3)){
            JOptionPane.showMessageDialog(null, "Orden: "+num1+" - "+num2+" - "+num3);
        }else if((num1>num3) && (num3>num2)){
            JOptionPane.showMessageDialog(null, "Orden: "+num1+" - "+num3+" - "+num2);
        }else if((num2>num1) && (num1>num3)){
            JOptionPane.showMessageDialog(null, "Orden: "+num2+" - "+num1+" - "+num3);
        }else if((num2>num3) && (num3>num1)){
            JOptionPane.showMessageDialog(null, "Orden: "+num2+" - "+num3+" - "+num1);
        }else if((num3>num1) && (num1>num2)){
            JOptionPane.showMessageDialog(null, "Orden: "+num3+" - "+num1+" - "+num2);
        }else{
            JOptionPane.showMessageDialog(null, "Orden: "+num3+" - "+num2+" - "+num1);
        }

    }
}
