/*
                            Throwable
            Exception                               Error(Hardware)
IOException         RunTimeException
(Exc. Verificadas)  (Exc. no Verificadas)


Exc. Verificadas: no depende total% del programador, tiene que ver con las entradas y salidas del programa,
                  leer un arch. que no existe (que se alguien lo borró).

Exc. no Verificadas: depende del programador, la división entre 0, guardar un String en una variable entera.
 */

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger;

public class PruebaExcepciones {

    public static void main(String[] args) throws FileNotFoundException, IOException { //si existe un IOE. se lanza
    /*
        //Exc. Verificadas (IOException)
            //Lectura de nu arch de texto (.txt)
            BufferedReader bf = new BufferedReader(new FileReader("C:\\Users\\joseb\\Escritorio\\ATS\\src\\texto.txt"));
            String linea; //  ya no existe el arch texto.txt
            try{
                while((linea=bf.readLine())!=null){
                    System.out.println(linea);
                }
            }catch (IOException ex){
                Logger.getLogger(PruebaExcepciones.class.getName()).log(Level"no se q va aquí xd");
                //Se puede poner arriba el IOE o usar el try-catch
    }
    */

        //Exc. no verificadas(RunTimeExcepcion)
        //División entre 0
        int num1 = 5, num2 = 0, resultado;

        resultado = num1 / num2;

        System.out.println(resultado);


    }
}
