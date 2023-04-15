public abstract class Area_poligonos {
    protected int numeroLados;

    public Area_poligonos(int numeroLados) {
        this.numeroLados = numeroLados;
    }

    public int getNumeroLados() {
        return numeroLados;
    }


    @Override
    public String toString() { //Es lo mismo que la función mostrarDatos()
        return "numeroLados=" + numeroLados +
                '}';
    }

    public abstract double area();
}
