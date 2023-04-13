//Encapsulamiento y Métodos accesores (Setters y Getters)
package src;

public class Clase1 {
    private int edad; //como es privado solo pueden acceder los métodos de la misma clase
    private String nombre;

    //Método Setter
    public void setEdad(int edad){
        this.edad = edad;
    }

    //Método Getter
    public int getEdad(){
        return edad;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getNombre() {
        return nombre;
    }


}
