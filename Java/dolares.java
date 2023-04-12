import java.util.Scanner;
import java.util.concurrent.ThreadPoolExecutor;

public class dolares {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int Guillermo, Luis, Juan, Total;
        System.out.println("Cuánto dinero tiene guillermo: ");
        Guillermo = entrada.nextInt();
        Luis = Guillermo/2;
        Juan = (Guillermo+Luis)/2;

        Total = Guillermo + Luis + Juan;

        System.out.println("El total de dinero que hay es: "+ Total);
    }
}
