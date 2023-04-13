import javax.swing.JOptionPane;

public class mayuscula {
    public static void main(String[] args) {
        char letra;
        letra = JOptionPane.showInputDialog("Digita un caracter: ").charAt(0); //sacamos el primer caracter del string

        if(Character.isUpperCase(letra)){
            JOptionPane.showMessageDialog(null, "La letra es mayuscula");
        }else{
            JOptionPane.showMessageDialog(null, "La letra es minúsicula");
        }


    }
}