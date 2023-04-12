import java.rmi.MarshalException;

public class math {
    public static void main(String[] args){
        //Raiz
        double raiz = Math.sqrt(9); //tiene que ser double el parámetro de sqtr
        int raiz2 = (int)Math.sqrt(9); //lo transformamos a int

        //Potencia
        double base = 5, exponente = 2;
        double potencia = Math.pow(5,2); //tmb deben ser doubles

        //redondeo
        double num = 4.64;
        float num2 = 4.64f;
        long resultado = Math.round(num);
        int resultado2 = Math.round(num2);

        //random
        double rand = Math.random();


        System.out.println(raiz);
        System.out.println(raiz2);

        System.out.println(potencia);

        System.out.println(resultado);
        System.out.println(resultado2);

        System.out.println(rand);

    }
}
