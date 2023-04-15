public class Main_polimorfismo {
    public static void main(String[] args){
        Vehiculo_polimorfismo misVehiculos[] = new Vehiculo_polimorfismo[4];

        misVehiculos[0] = new Vehiculo_polimorfismo("GH67", "Ferrari", "A23");
        misVehiculos[1] = new Vehiculo_polimorfismo_turismo("78HJ","Audi", "P14", 4);
        misVehiculos[2] = new Vehiculo_polimorfismo_deportivo("45GH", "Toyota", "KJ8", 500);
        misVehiculos[3] = new Vehiculo_polimorfismo_furgoneta("JI8", "Toyota", "J9", 2000);

        for(Vehiculo_polimorfismo vehiculos:misVehiculos){
            System.out.println(vehiculos.mostrarDatos());
            System.out.println("");
        }
    }
}
