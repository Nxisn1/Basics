//Miembros estáticos de una clase o miembros de clase

public class Estatico {
    private static String frase="Primera frase"; //frase ya no le pertenece a los objetos,sino que le pertenece a la clase
    /* o sea que todos los cambios que se le haga a frase, será para todos lo objetos */

    public static int sumar(int n1, int n2){ //método estático
        int suma = n1+n2;
        return suma;
    }

    public static void main(String[] args){
        System.out.println(Estatico.frase); //como frase es de la clase, no es necesario crear un objeto para llamarla
        System.out.println("La suma es: "+Estatico.sumar(3,4)); //simple% llamamos al método con la clase, sin objeto

    }
}
