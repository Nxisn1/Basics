public class Vehiculo_polimorfismo_furgoneta extends Vehiculo_polimorfismo{
    private int carga;

    public Vehiculo_polimorfismo_furgoneta(String matricula, String marca, String modelo, int carga) {
        super(matricula, marca, modelo);
        this.carga = carga;
    }

    public int getCarga() {
        return carga;
    }

    @Override
    public String mostrarDatos(){
        return "Matricla: "+matricula+"\nMarca: "+marca+"\nModelo: "+modelo+"\nCarga: "+carga;
    }
}
