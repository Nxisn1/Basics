import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.*;

public class Eventos extends JFrame{
    private JPanel panel;
    private JLabel saludo;
    private JTextField cajaTexto;
    private JButton boton;


    public Eventos(){
        setBounds(50,50,500,500);
        setTitle("Eventos");
        iniciarComponentes();
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    private void iniciarComponentes(){
        colocarPanel();
        colocarEtiqueta();
        colocarCajaDeTexto();
        colocarBoton();
    }

    private void colocarPanel(){
        panel = new JPanel();
        panel.setLayout(null);
        this.add(panel);
    }

    private void colocarEtiqueta(){
        JLabel etiqueta = new JLabel("Ingrese su nombre: ");
        etiqueta.setBounds(30,10,300,30);
        etiqueta.setFont(new Font("cooper black", Font.BOLD, 20));
        panel.add(etiqueta);
    }

    private void colocarCajaDeTexto(){
        cajaTexto = new JTextField();
        cajaTexto.setBounds(30,50,300,30);
        panel.add(cajaTexto);
    }




    private void colocarBoton(){
        boton = new JButton("¡Pulsa aquí!");
         boton.setBounds(150,100,150,40);
        boton.setFont(new Font("arial",0,15));
        panel.add(boton);

        eventoOyenteDeAccion();
    }

    private void eventoOyenteDeAccion(){
        saludo = new JLabel();
        saludo.setBounds(50,200,300,40);
        saludo.setFont(new Font("arial",1,20));
        panel.add(saludo);

        //Agregando Evento de tipo ActionListen
        ActionListener oyenteDeAccion = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent ae) {
                saludo.setText("Hola "+cajaTexto.getText());
            }
        };

        boton.addActionListener(oyenteDeAccion);
    }

}
