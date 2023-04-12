import java.util.Scanner;


public class operadores {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        float numero1, numero2, suma, resta, mult, div, resto;

        System.out.print("digita dos números: ");
        numero1 = entrada.nextFloat();
        numero2 = entrada.nextFloat();

        suma = numero1 + numero2;
        resta = numero1 - numero2;
        mult = numero1 * numero2;
        div = numero1 / numero2;
        resto = numero1 % numero2;

        System.out.println("la suma es: "+suma );
        System.out.println("la suma es: "+ resta);
        System.out.println("la suma es: "+ mult);
        System.out.println("la suma es: "+ div);
        System.out.println("la suma es: "+ resto);

        int numero = 10;
        numero += 5; //numero = numero + 5
        numero -= 5;
        numero *= 5;
        numero /= 5;
        numero %= 5;
        numero++; //se incrementa en 1,  tmb se puede poner al principio ++x
        numero--; //se decrementa en 1,  --numero
        System.out.println(numero);

    }
}
