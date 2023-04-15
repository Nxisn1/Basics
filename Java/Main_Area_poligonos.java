import java.util.ArrayList;
import java.util.Scanner;

public class Main_Area_poligonos {
    static ArrayList<Area_poligonos> poligono = new ArrayList<Area_poligonos>();
    static Scanner entrada = new Scanner(System.in);
    public static void main(String[] args){
        //llenar un poligono
        llenarPoligono();

        //mostrar datos y area de cada poligono
        mostrarResultados();
    }

    public static void llenarPoligono(){
        char respuesta;
        int opcion;
        do{
            do{
                System.out.println("Digite que poligono desea");
                System.out.println("1. Triangulo");
                System.out.println("2. Rectangulo");
                System.out.println("Opción: ");
                opcion = entrada.nextInt();
            }while(opcion<1 || opcion>2);

            switch (opcion){
                case 1: llenarTriangulo();
                    break;
                case 2: llenarRectangulo();
                    break;
            }

            System.out.print("\nDesea introducir otro poligono(s/n): ");
            respuesta = entrada.next().charAt(0);
            System.out.println("");
        }while(respuesta=='s' || respuesta=='S');
    }

    public static void llenarTriangulo(){
        double lado1, lado2, lado3;

        System.out.print("\nDigite el lado1 del triangulo: ");
        lado1 = entrada.nextDouble();
        System.out.print("\nDigite el lado2 del triangulo: ");
        lado2 = entrada.nextDouble();
        System.out.print("\nDigite el lado3 del triangulo: ");
        lado3 = entrada.nextDouble();

        Triangulo_Area_poligonos triangulo = new Triangulo_Area_poligonos(lado1, lado2, lado3);
        //Guardamos un triangulo dentro de nuestro arreglo de poligonos
        poligono.add(triangulo);
    }

    public static void llenarRectangulo() {
        double lado1, lado2;
        System.out.print("\nDigite el lado1 del rectangulo: ");
        lado1 = entrada.nextDouble();
        System.out.print("\nDigite el lado2 del rectangulo: ");
        lado2 = entrada.nextDouble();

        Rectangulo_Area_poligonos  rectangulo = new Rectangulo_Area_poligonos(lado1, lado2);
        poligono.add(rectangulo);
    }

    public static void mostrarResultados(){
        //Recorriendo el arreglo de poligonos
        for(Area_poligonos poli: poligono){
            System.out.println(poli.toString());
            System.out.println("Area: "+poli.area());
            System.out.println("");
        }
    }




}
