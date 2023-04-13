import java.util.Scanner;

public class if_else {
    public static void main(String[] args){
        int dato;
        Scanner entrada = new Scanner(System.in);
        System.out.println("ingresa un número: ");
        dato = entrada.nextInt();

        if(dato <10){
            System.out.println("dato es menor que 10");
        }else{
            System.out.println("dato es mayor que 10");
        }
    }
}
