public class Persona_herencia {
    private String nombre; // con el protected pueden ser accedido por los miembros de la clase y además por las clase hijas
    private String apellido;
    private int edad;

    public Persona_herencia(String nombre, String apellido, int edad) {
        this.nombre = nombre;
        this.apellido = apellido;
        this.edad = edad;
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public int getEdad() {
        return edad;
    }

    //Sobre escritura de miembros
    public String comer(){
        return "Estoy comiendo.";
    }



}
