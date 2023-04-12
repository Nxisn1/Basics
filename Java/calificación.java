import java.util.Scanner;

public class calificación {
    public static void main(String[] args){
        float N_participacion, N_primer_examen, N_segundo_examen, N_examen_final, calificacion_final;
        Scanner entrada = new Scanner(System.in);
        System.out.println("Ingresa tus notas de participación, primer examen, segundo examen y examne final: ");
        N_participacion = entrada.nextFloat();
        N_primer_examen = entrada.nextFloat();
        N_segundo_examen = entrada.nextFloat();
        N_examen_final = entrada.nextFloat();

        calificacion_final =  (N_participacion*0.1f) + (N_primer_examen*0.25f) + (N_segundo_examen*0.25f) + (N_examen_final*0.4f);
        System.out.println("tu nota final es: "+ calificacion_final);
    }
}
