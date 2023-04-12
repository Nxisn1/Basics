import java.util.Scanner;

public class promedio {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        float nota1, nota2, nota3, promedio;

        System.out.println("Ingresa tus 3 notas: ");
        nota1 = entrada.nextFloat();
        nota2 = entrada.nextFloat();
        nota3 = entrada.nextFloat();

        promedio = (nota2+nota1+nota3)/3;
        System.out.println("tu promedio es: "+ promedio);
    }
}
