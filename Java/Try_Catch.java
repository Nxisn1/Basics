import java.io.*;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.swing.JOptionPane;

//El try_catch nos sirve para que si salta una Exc. el programa no se detenga.
public class Try_Catch {

    public void leerArchivo() throws FileNotFoundException, IOException{
        File archivo = new File("C:\\direccion\\texto.txt");
        FileReader fr = new FileReader(archivo);
        BufferedReader bf = new BufferedReader(fr);
        String linea;
    }

    public void leerArchivo2(){
        try{
            leerArchivo(); //aquí va lo q puede tener una excepción
        }catch (FileNotFoundException ex) { //en caso de que suceda una excepción usamos catch (capturar la excepción). tenemos que ponerle  nombre, ex es el nombre
            JOptionPane.showMessageDialog(null, "No se ha encontrado el archivo .");
        }catch (IOException e){
            JOptionPane.showMessageDialog(null, "Ha ocurrido una excepción verificada.");
        }

        System.out.println("Programa terminado");
    }


    public static void main(String[] args){
         Try_Catch prueba = new Try_Catch();

         prueba.leerArchivo2(); //no tiera error, sino que tira el JOP con 'No se ha encontrado archivo'
    }


}
