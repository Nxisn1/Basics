public class Vehiculo_polimorfismo_turismo extends Vehiculo_polimorfismo {
    private int nPuertas;

    public Vehiculo_polimorfismo_turismo(String matricula, String marca, String modelo, int nPuertas) {
        super(matricula, marca, modelo);
        this.nPuertas = nPuertas;
    }

    public int getnPuertas() {
        return nPuertas;
    }

    @Override
    public String mostrarDatos(){
        return "Matricla: "+matricula+"\nMarca: "+marca+"\nModelo: "+modelo+"\nNúmero de puertas: "+nPuertas;
    }

}
