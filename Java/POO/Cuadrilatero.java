/*
    Programa que calcual el área y perímetro de un cuadrilátero dada la longitud de sus dos lados. Si es un cuadrado solo
    se proporciona la longitud de unos de los lados al constructor.
 */

public class Cuadrilatero {
    private float lado1;
    private float lado2;

    //Método Constructor 1 (Cuadrilatero)
    public Cuadrilatero(float lado1, float lado2) {
        this.lado1 = lado1;
        this.lado2 = lado2;
    }

    //Método Constructor 2 (Cuadrado)
    public Cuadrilatero(float lado1) {
        this.lado1 = this.lado2 = lado1;
    }

    //Getters
    public float getPetimetro(){
        float perimetro = 2 * (lado1+lado2);
        return perimetro;
    }

    public float getArea(){
        float area = (lado1*lado2);
        return area;
    }


}
