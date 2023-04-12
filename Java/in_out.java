import java.util.Scanner; //lib para usar Scanner


public class in_out {

    public static void main(String[] args){

        Scanner entrada_int = new Scanner(System.in);
        int entero;
        System.out.print("Ingresa un número entero: ");
        entero = entrada_int.nextInt();

        Scanner entrada_float = new Scanner(System.in);
        float decimal;
        System.out.print("Ingresa un número decimal: "); //Se debe poner con coma (,) con punto (.) tira error
        decimal = entrada_float.nextFloat();

        Scanner entrada_cadena = new Scanner(System.in);
        String cadena;
        System.out.print("Digita una cadena: ");
        cadena = entrada_cadena.next(); //lo guarda solo hasta el espacio

        Scanner entrada_cadena_extensa = new Scanner(System.in);
        String cadena_extensa;
        System.out.print("Digita una cadena extensa: ");
        cadena_extensa = entrada_cadena_extensa.nextLine();

        Scanner entrada_primer_caracter = new Scanner(System.in);
        char primer_caracter;
        System.out.print("Digita una palabra, pero solo se verá el primer caracter: ");
        primer_caracter = entrada_primer_caracter.next().charAt(0); //el cero es el primer caracter, usa el índice del q quieras


        System.out.println("el número entero es: "+entero);
        System.out.println("el número decimales: "+decimal);
        System.out.println("la cadena es: "+cadena);
        System.out.println("la cadena_extensa es: "+cadena_extensa);
        System.out.println("el primer carcter es: "+primer_caracter);


    }
}
