public class variables {
    public static void main(String[] args){
    //Datos primitivos

            //Enteros
                byte entero = 12;
                short entero_2 = 12345;
                int entero_3 = 43242;
                long entero_4 = 123487;
            //Decimales
                float decimal = 3.15f;
                double decimal_2 = 3.12345;

            //caracteres
                char caracter  = 'a'; //comillas simples
                char caracter_2  = '1';

            //lógico
                boolean decision_1 = false;
                boolean decision_2 = true;

    //Datos no primitivos (con los no primitivos tenemos funciones)

            Integer numero = 1;
            Integer numero_2 = null;

            //cadenas
            String palabra = "Hola"; //comillas dobles

    //constante
            final int num = 10; //no se puede modificar su valor, final lo hace const.

    //prints
            //Enteros
                System.out.println("Numero entero byte: "+ entero);
                System.out.println("Numero entero_2 short: "+ entero_2);
                System.out.println("Numero entero_3 int: "+ entero_3);
                System.out.println("Numero entero_4 longs: "+ entero_4);
            //Decimales
                System.out.println("Numero decimal float: "+ decimal);
                System.out.println("Numero decimal_2 float: "+ decimal_2);
            //caracteres
                System.out.println("caracter: "+ caracter);
                System.out.println("caracter_2: "+ caracter_2);
            //lógicos
                System.out.println("decision_1: "+ decision_1);
                System.out.println("decision_2 : "+ decision_2);


            System.out.println(palabra);


    }
}
