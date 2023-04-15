import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class PruebaExcepciones2 {

    public void leerArchivo() throws FileNotFoundException{
        File archivo = new File("C:\\direccion\\texto.txt");
        FileReader fr = new FileReader(archivo);
    }

    public void leerArchivo2() throws IOException{ //podemos poner las excepciones en las super
        leerArchivo();
    }

    public static void main(String[] args){

    }

}