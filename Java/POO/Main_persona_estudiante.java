public class Main_persona_estudiante {
    public static void main(String[] args){
        Persona_herencia persona = new Persona_herencia("Pepe", "Piña", 21);

        Estudiante_herencia estudiante = new Estudiante_herencia("Alejandro", "Taboada", 21, 123, 15.6f);
        estudiante.mostrarDatos();

        System.out.println("Método comer del estudiante: "+estudiante.comer());
        System.out.println("Método comer de la persona: "+persona.comer());



    }
}
