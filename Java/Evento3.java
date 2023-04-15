import java.awt.*;
import java.awt.event.*;
import java.security.Key;
import javax.swing.*;

public class Evento3 extends JFrame{
    private JPanel panel;
    private JButton boton;

    private JTextArea areaTexto;
    private JTextField cajaTexto;

    public Evento3(){
        setBounds(50,50,500,500);
        setTitle("Eventos");
        iniciarComponentes();
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    private void iniciarComponentes() {
        colocarPanel();
        colocarCajaDeTexto();
        colocarAreaDeTexto();
    }

    private void colocarPanel(){
        panel = new JPanel();
        panel.setLayout(null);
        this.add(panel);
    }


    private void colocarCajaDeTexto(){
        cajaTexto = new JTextField();
        cajaTexto.setBounds(20,30,150,30);
        panel.add(cajaTexto);

        eventosDelTeclado();
    }

    private void colocarAreaDeTexto(){
        areaTexto = new JTextArea();
        areaTexto.setBounds(230,30,200,300);
        panel.add(areaTexto);

        JScrollPane scroll = new JScrollPane(areaTexto,ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS,ScrollPaneConstants.HORIZONTAL_SCROLLBAR_ALWAYS);
        scroll.setBounds(230,30,200,300);
        panel.add(scroll);
    }


    private void eventosDelTeclado(){
        KeyListener eventoTeclado = new KeyListener() {
            @Override
            public void keyTyped(KeyEvent ke) { //Solo admite caracteres unique (excluye alt, ctrl, los de ese tipo)
                areaTexto.append("keyTyped\n");

            }

            @Override
            public void keyPressed(KeyEvent ke) {
                areaTexto.append("keyPressed\n");
            }

            @Override
            public void keyReleased(KeyEvent ke) { //presionar y soltar, cualquier tecla
                areaTexto.append("keyReleased\n");
                if(ke.getKeyChar() == 'p'){
                    areaTexto.append("Letra p\n");
                }if(ke.getKeyChar() == '\n'){
                    areaTexto.append("Enter\n");
                }if(ke.getKeyChar() == ' '){
                    areaTexto.append("Espacio\n");
                }
            }
        };

        cajaTexto.addKeyListener(eventoTeclado);
    }

}


