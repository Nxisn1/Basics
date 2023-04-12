import javax.swing.JOptionPane;

public class in_out_joptionpane {
    public static void main(String[] args){

        String cadena;
        int entero;
        char letra;
        double decimal;

        cadena = JOptionPane.showInputDialog("Digita una cadena: ");
        entero = Integer.parseInt(JOptionPane.showInputDialog("Digita una entero: ")); //el jop te da un string, con lo primero lo pasamos a int
        letra = JOptionPane.showInputDialog("Digita un caracter: ").charAt(0); //sacamos el primer caracter del string
        decimal = Double.parseDouble(JOptionPane.showInputDialog("Digita un decimal: ")); //lo pasamos a double, se pasa con punto (.) sino error.

        JOptionPane.showMessageDialog(null, "La cadena es:"+cadena);
        JOptionPane.showMessageDialog(null, "El entero es:"+entero);
        JOptionPane.showMessageDialog(null, "La letra es:"+letra);
        JOptionPane.showMessageDialog(null, "El decimal es:"+decimal);


    }
}
