public class Estudiante_herencia extends Persona_herencia { //Estudiante hereda de Persona
    private int codigoEstudainte;
    private float notaFinal;

    public Estudiante_herencia(String nombre, String apellido, int edad, int codigoEstudainte, float notaFinal) {
        super(nombre, apellido, edad);
        this.codigoEstudainte = codigoEstudainte;
        this.notaFinal = notaFinal;
    }

    public void mostrarDatos(){
        System.out.println("Nombre: "+getNombre()+
                "\nApellido"+getApellido()+
                "\n Edad: "+getEdad()+
                "\nCódigo del estudiante: "+codigoEstudainte+
                "\nNota final: "+notaFinal);
    }

    @Override //sobre escritura de miembros
    public String comer(){
        return "Soy estudiante, no como.";
    }


}
