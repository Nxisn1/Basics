import java.util.Scanner;

public class ciclos{
    public static void main(String[] args) {

        //while
        int i=1;
        while(i<=10){
            System.out.println(i);
            i++;
        }


        //do-while
        int j = 11;
        do{
            System.out.println(j);
            j++;
        }while(j<=10);


        /*for(inicialización ; condición ; aumento o decremento){
            Intrucciones;
        }
        */
        for(int f=1; f<=10; f++){
            System.out.println(f);
        }

    }
}