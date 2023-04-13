public class for_each {
    public static void main(String[] args){

        String[] nombres = {"Ale", "Maria", "Luisa", "Juan", "Jose", "pepe"}; //nombres.length nos da la cantidad de elementos del arreglo

        //for(tipo_dato i:arreglo)
        for(String i:nombres){
            System.out.println("Nombre: "+ i);
        }

    }
}
