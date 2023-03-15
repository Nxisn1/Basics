/*
 * -clase: prototipo que define las variables y métodos comunes a un cierto tipo de instancia (plantilla para la creación
            de objetos).
 *      -variables: lo que lo diferencia de las otras.
 *      -método: acciones que puede realizar.
 *
 *   final: es parecido a las constantes en otros lenguajes, su valor no puede ser modificado una vez inicializado,
 *   identificador en mayusculas.
 *      final int MAXIMO = 15; 
 * 
 *  Convertir a byte code: 'javac arch.java'
 *      extensión byte code: .class
 *  luego ejecutar 'java arch'
 *
 *
 */

package com.mycompany.aprendiendo;
import java.util.Scanner; //librería para input del user.

public class Aprendiendo {
    public static void main(String[] args) {
        
        String x = "Hola";
        String y = "Hola";
        Boolean match; 
        int i = 0;
        int[] numbers = {39,23,2543,102}; 
        
        match = x.equals(y);
        
        if(match == true){
            System.out.println("son iguales");
        }else{
            System.out.println("No son iguales");
        }
        
        Scanner Aux = new Scanner(System.in);
        System.out.println("Ingresa tu edad");
        
        String Edad_user = Aux.nextLine();
        System.out.printf("tiene %s\n", Edad_user);
        
        while(i<5){
            System.out.printf("%d\n", i); //va desde el 0 al 4
            i++;
                    
        }
      
        for(int j=0; j<numbers.length; j++){
            System.out.printf("%d\n", numbers[j]);
        }
        

        
        
    }
}


