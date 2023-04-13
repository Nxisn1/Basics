import java.util.Scanner;
import java.util.concurrent.TransferQueue;

public class Main_isosceles {
    public static double mayorArea(Isosceles triangulos[]){
        double area;

        area = triangulos[0].obtenerArea();

        for(int i=0; i<triangulos.length; i++){
            if(triangulos[i].obtenerArea() > area){
                area = triangulos[i].obtenerArea();
            }
        }
        return area;
    }

    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        double base, lado;
        int nTriangulos;

        System.out.print("Digite el número de triangulos: ");
        nTriangulos = entrada.nextInt();

        Isosceles triangulos[] = new Isosceles[nTriangulos];

        for(int i=0; i<nTriangulos; i++){
            System.out.println("\nDigite los valores para el triangulo "+(i+1)+": ");
            System.out.print("Digite la base: ");
            base = entrada.nextDouble();
            System.out.print("Digite el lado: ");
            lado = entrada.nextDouble();

            triangulos[i] = new Isosceles(base, lado);

            System.out.println("\nEl perimetro del trianguilo es: "+triangulos[i].obtenerPerimetro());
            System.out.println("\nEl Área del trianguilo es: "+triangulos[i].obtenerArea());

        }

        System.out.println("\nEl area del triangulo de mayor superficie es: "+ mayorArea(triangulos));

    }

}
