
public class Auto {
    //Atributos
    String color;
    String marca;
    int km;

    //Metodo
    public static void main(String[] args){
        Auto Auto1 = new Auto();

        Auto1.color = "Blanco";
        Auto1.marca = "Audi";
        Auto1.km = 0;

        System.out.println("El color del Auto1 es: "+Auto1.color);
        System.out.println("La marca del Auto1 es: "+Auto1.marca);
        System.out.println("El km del Auto1 es: "+Auto1.km);

        Auto Auto2 = new Auto();
        Auto2.color = "Rojo";
        Auto2.marca = "Ferrari";
        Auto2.km = 100;

        System.out.println("El color del Auto2 es: "+Auto2.color);
        System.out.println("La marca del Auto2 es: "+Auto2.marca);
        System.out.println("El km del Auto2 es: "+Auto2.km);

    }
}
