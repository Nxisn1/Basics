public class Vehiculo_polimorfismo {
    protected String matricula;
    protected String marca;
    protected String modelo;

    public Vehiculo_polimorfismo(String matricula, String marca, String modelo) {
        this.matricula = matricula;
        this.marca = marca;
        this.modelo = modelo;
    }

    public String getMatricula() {
        return matricula;
    }

    public String getMarca() {
        return marca;
    }

    public String getModelo() {
        return modelo;
    }

    public String mostrarDatos(){
        return "Matricla: "+matricula+"\nMarca: "+marca+"\nModelo: "+modelo;
    }
}

