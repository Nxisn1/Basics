public class Main_persona {
    public static void main(String[] args){

        src.Persona_constructor p1 = new src.Persona_constructor("Alejandro", 21); //se usa el primer constructor
        //src.Persona_constructor p2 = new src.Persona_constructor(2343212); //Se usa el segundo constructor

        p1.mostrarDatos();


        p1.correr();
        p1.correr(12);
    }
}
