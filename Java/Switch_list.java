/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 *
 * nextLine();
 * nextBoolean()	Reads a boolean value from the user
 * nextByte()	Reads a byte value from the user
 * nextDouble()	Reads a double value from the user
 * nextFloat()	Reads a float value from the user
 * nextInt()	Reads a int value from the user
 * nextLine()	Reads a String value from the user
 * nextLong()	Reads a long value from the user
 * nextShort()	Reads a short value from the user
 *
 *
 *
 *
 *
*/
package com.mycompany.aprendiendo;

/**
 *
 * @author joseb
 */

import java.util.Scanner;  // Import the Scanner class

public class input_list {
    public static void main(String[] args) {
       
    int sw;
    String sw_list;
    int[] numbers = {12,43,54};
    String[] names = {"pepe", "juan", "pedro"};
    
    Scanner Aux_sw = new Scanner(System.in);  // Create a Scanner object
    System.out.println("Ingresa un número para probar el switch");

    sw = Aux_sw.nextInt();  // Read user input
    
    switch (sw) {
        case 1:
            System.out.println("Ingresaste en el caso 1.");
            break;
        case 2:
            System.out.println("Ingresaste en el caso 2.");
            break;
        default:
            System.out.println("Ingresaste en el caso predeterminado.");
    }
        
       
    Scanner sw_numbers_or_names = new Scanner(System.in);  // Create a Scanner object
    System.out.println("Quieres la lista de los números o de los nombres");

    sw_list = sw_numbers_or_names.nextLine();  // Read user input
    
    switch (sw_list) {
        case "numbers":
            for(int i=0; i<numbers.length; i++){
                System.out.printf("%d\n", numbers[i]);
            }
            break;
        case "names":
            for(int i=0; i<names.length; i++){
                System.out.printf("%s\n", names[i]);
            }
            break;
        default:
            System.out.println("Tienes que ingresar names o numbers.");
        }
    }
}
