public class Vehiculo_polimorfismo_deportivo extends Vehiculo_polimorfismo{
    private int cilindrada;

    public Vehiculo_polimorfismo_deportivo(String matricula, String marca, String modelo, int cilindrada) {
        super(matricula, marca, modelo);
        this.cilindrada = cilindrada;
    }

    public int getCilindrada() {
        return cilindrada;
    }

    @Override
    public String mostrarDatos(){
        return "Matricla: "+matricula+"\nMarca: "+marca+"\nModelo: "+modelo+"\nCilindrada: "+cilindrada;
    }
}
