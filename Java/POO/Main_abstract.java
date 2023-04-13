import java.security.Provider;

public class Main_abstract {
    public static void main(String[] args){

        //SerVivo_abstract servivo = new SerVivo_abstract(); //no se puede crear objetos de clases abstractas

        Planta_abstract planta = new Planta_abstract();
        AnimalCarnivoro_abstract animalC = new AnimalCarnivoro_abstract();
        AnimalHerbivoro_abstract animalH = new AnimalHerbivoro_abstract();

        planta.alimentarse();
        animalC.alimentarse();
        animalH.alimentarse();

    }
}
