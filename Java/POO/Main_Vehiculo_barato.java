import java.util.Scanner;

public class Main_Vehiculo_barato {

    public static int indice_AutoMBarato(Vehiculo_barato autos[]){
        float precio;
        int indice = 0;

        precio = autos[0].getPrecio();
        for(int i=1; i<autos.length; i++){
            if(autos[i].getPrecio() < precio){
                precio = autos[i].getPrecio();
                indice = i;
            }
        }
        return indice;
    }

    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        String marca, modelo;
        float precio;
        int numero_vehiculos, indiceBarato;


        System.out.print("Digita el número de vehiculos: ");
        numero_vehiculos = entrada.nextInt();

        //Creamos los objetos para los auto
        Vehiculo_barato autos[] = new Vehiculo_barato[numero_vehiculos];

        for(int i=0; i<autos.length; i++) { //numero_vehiculos == autos.lenght, lenght da la cantidad de elementos del arreglo
            entrada.nextLine(); //Esto es pq al ejecutar salía 'Marca: Modelo:' pegados entonces es para 'despegarlos'
            System.out.println("\nDigita las caracteristicas del auto "+(i+1)+":");
            System.out.print("Marca: ");
            marca = entrada.nextLine();
            System.out.print("Modelo: ");
            modelo = entrada.nextLine();
            System.out.print("Precio: ");
            precio = entrada.nextFloat();

            autos[i] = new Vehiculo_barato(marca, modelo, precio);
        }


        indiceBarato = indice_AutoMBarato(autos);
        System.out.println("");
        System.out.println("El auto más barato es: ");
        System.out.println(autos[indiceBarato].mostrarDatos());

    }
}
