import javax.swing.JOptionPane;

public class multiplo10 {
    public static void main(String[] args){
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digita una entero: ")); //el jop te da un string, con lo primero lo pasamos a int

        if(numero%10==0){
            JOptionPane.showMessageDialog(null, "El numero es multiplo de 10");
        }else{
            JOptionPane.showMessageDialog(null, "El numero NO es multiplo de 10");

        }
    }
}
