import java.util.Scanner;

public class switchh {
    public static void main(String[] args){
        int dato;
        Scanner entrada = new Scanner(System.in);
        System.out.println("ingresa un número: ");
        dato = entrada.nextInt();

        switch(dato){
            case 1: System.out.println("ingresaste 1");
                break;
            case 2: System.out.println("ingresaste 2 ");
                break;
            case 3: System.out.println("ingresaste 3 ");
                break;
            default: System.out.println("no ingresaste ni 1 ni 2 ni 3");
        }
    }
}