//búsqueda de un elemento dentro de un arreglo

import javax.swing.*;

public class busqueda_secuencial {
    public static void main(String[] args){

        int arreglo[] = {4,1,3,5,2};
        int dato;
        boolean flag = false;

        dato = Integer.parseInt(JOptionPane.showInputDialog("Digíta el número a buscar"));

        //Búsqueda secuencial
        int i=0;
        while(i<5 && flag==false) { //el 5 es el número de elementos del arreglo.
            if(arreglo[i] == dato){
                flag = true;
            }
            i++;
        }
        if(flag == false){
            JOptionPane.showMessageDialog(null, "El número no se encontró");
        }else{
            JOptionPane.showMessageDialog(null, "El número ha sido encontrado en la pos: "+(i-1) );
        }
    }
}
