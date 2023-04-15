import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import javax.swing.*;

public class Eventos2 extends JFrame{
    private JPanel panel;
    private JButton boton;

    private JTextArea areaTexto;

    public Eventos2(){
        setBounds(50,50,500,500);
        setTitle("Eventos");
        iniciarComponentes();
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    private void iniciarComponentes() {
        colocarPanel();
        colocarBoton();
        colocarAreaDeTexto();
    }

    private void colocarPanel(){
        panel = new JPanel();
        panel.setLayout(null);
        this.add(panel);
    }

    private void colocarBoton(){
        boton = new JButton("¡Pulsa aquí!");
        boton.setBounds(150,350,150,40);
        boton.setFont(new Font("arial",0,15));
        panel.add(boton);

    }
    private void colocarAreaDeTexto(){
        areaTexto = new JTextArea();
        areaTexto.setBounds(20,20,200,300);
        panel.add(areaTexto);

        eventoOyenteDeRaton();
    }

    private void eventoOyenteDeRaton(){
        //Agregando oyente de Ratón - MouseListener
        MouseListener oyenteDeRaton = new MouseListener() {
            @Override
            public void mouseClicked(MouseEvent me) { //presionar y soltar dentro del botón
                areaTexto.append("mouseClicked\n");
            }

            @Override
            public void mousePressed(MouseEvent me) {
                areaTexto.append("mousePressed\n");
            }

            @Override
            public void mouseReleased(MouseEvent me) { //presionar y soltar, sirve tanto dentro como fuera del botón
                areaTexto.append("mouseReleased\n");

            }

            @Override
            public void mouseEntered(MouseEvent me) { //meter el click dentro del botón, sin presionar
                areaTexto.append("mouseEntered\n");
            }

            @Override
            public void mouseExited(MouseEvent me) { //Salir del botón
                areaTexto.append("mouseExited\n");

            }
        };

        //Esos eran eventos del mouse de click, también hay eventos de movimiento del ratón y de la rueda
        boton.addMouseListener(oyenteDeRaton);
    }


}


