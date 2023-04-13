package src;

public class Persona_constructor {
    //Atributos
    String nombre;
    int edad;
    String dni;

    //Métodos

    //Método constructor
    /*
    public Persona_constructor(String _nombre, int _edad){
        nombre = _nombre;
        edad = _edad;
    }
    */
    public Persona_constructor(String nombre, int edad){ //es igual al de arriba pero este es más bonito
        this.nombre = nombre; //'this' se refiere al atributo
        this.edad = edad;
    }

    public Persona_constructor(String dni) { //sobrecarga de constructores (más de un constructor)
        this.dni = dni;
    }

    public void mostrarDatos(){
        System.out.println("El nombre es: "+nombre);
        System.out.println(("La edad es: "+edad));
    }

    public void correr(){
        System.out.println("Soy "+nombre+", tengo "+edad+" años y estoy corriendo una maratón.");
    }

    public void correr(int km){ //Sobrecarga de métodos, se diferencias por los parámetros (la cantidad y el tipo).
        System.out.println("He corrido "+km+" kilometros");
        //java no diferencia los métodos por los retornos.
    }


}
