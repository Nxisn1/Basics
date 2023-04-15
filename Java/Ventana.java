import javax.swing.*; //con el * importas todas las clases de javax.swing, sino tendrias que importar cada una por separado
import java.awt.*;    //import javax.swing.JFrame/javax.swing.JPanel/javax.swing.JLabel

public class Ventana extends JFrame {

    public JPanel panel;
    public Ventana() {

        this.setSize(500, 500); //ancho, largo. Establecemos el tamaño de la ventana
        setTitle("El mejor título"); //Establecemos el título de la ventana
        //setLocation(100,200); // (x,y) Establecemos la posición inicial de la ventana
        //setBounds(100, 200, 500, 500); //este incluye el setSize y el setLocation //Establecemos posición inicial y tamaño
        setLocationRelativeTo(null); //Aparece la ventana en el centro de la pantalla

        setMinimumSize(new Dimension(200,200)); //Establecemos el tamaño mínimo
        //this.getContentPane().setBackground(Color.BLUE); //Establecer el color de la ventana

        iniciarComponentes();

        setDefaultCloseOperation(EXIT_ON_CLOSE); //cuando cerremos la venta automatica% el programa también va a finalizar

    }

    private void iniciarComponentes(){

        colocarPaneles();
        //colocarEtiquetas();
        //colocarBotones();
        //colocarRadioBotones();
        //colocarCajasDeTexto();
        //colocarAreasDeTexto();
        colocarListasDesplegables();
    }

    private void colocarPaneles(){
        //JPanel panel = new JPanel()
        panel = new JPanel(); //Creación de un panel

        //panel.setBackground(Color.GREEN); //Establecemos el color del panel
        panel.setLayout(null); //Desactivando el layout (Diseño)
        this.getContentPane().add(panel); //Agregamos el panel a la ventana
    }

    private void colocarEtiquetas(){
        //Etiqueta 1 - etiqueta tipo texto
        //JLabel etiqueta = new JLabel("Hola", SwingConstants.CENTER); //juntamos el setText() y setHorizontalAligment()
        JLabel etiqueta = new JLabel(); //Creamos una etiqueta
        etiqueta.setText("Hola"); //Establecemos el texto de la etiqueta
        etiqueta.setBounds(10,10,50,50);
        etiqueta.setHorizontalAlignment(SwingConstants.CENTER); //Establecemos la alineación horizontal del texto
        etiqueta.setForeground(Color.ORANGE); //Establecemos el color de la letra en la etiqueta
        etiqueta.setOpaque(true); //las etiquetas por default tienen el fondo transparente. Establecemos pintar el fondo de la etiqueta
        etiqueta.setBackground(Color.YELLOW); //Cambiamos el color del fondo de la etiqueta
        etiqueta.setFont(new Font("arial", Font.BOLD, 20)); //Establecemos la fuente del texto

        panel.add(etiqueta);  //Agregamos la etiqueta al panel

        //Etiqueta 2 - etiqueta tipo imagen
        //JLabel etiqueta2 = new JLabel(new ImageIcon("C:\\Users\\joseb\\Escritorio\\ATS\\src\\images.jpg"));
        ImageIcon imagen = new ImageIcon("C:\\direccion\\imagen.jpg");
        JLabel etiqueta2 = new JLabel(new ImageIcon());
        etiqueta2.setBounds(10, 80, 274, 184); //(x,y,ancho,largo)
        etiqueta2.setIcon(new ImageIcon(imagen.getImage().getScaledInstance(etiqueta2.getWidth(), etiqueta2.getHeight(), Image.SCALE_SMOOTH)));

        panel.add(etiqueta2);
    }

    private void colocarBotones(){
        //Botón 1 - botón de texto
        JButton boton1 = new JButton();
        boton1.setText("Click"); //Establecemos un texto a botón
        boton1.setBounds(100, 100, 100, 40);
        boton1.setEnabled(true); //habilitar o deshabilitar botón
        boton1.setMnemonic('a'); //EStablecemos que el botón funciones con alt+a
        boton1.setForeground(Color.BLACK); //Color de la letra del botón
        boton1.setFont(new Font("arial", Font.BOLD, 30)); //Fuente de la letra del botón

        panel.add(boton1);

        //Botón 2 - botón de imagen
        JButton boton2 = new JButton();
        boton2.setBounds(100,200,100,40);
        //boton2.setOpaque(true); //hay algunas versiones de java q no dejan simplemente cambiar el color por eso esta linea, que dice que nos da 'permiso' de cambiarlo
        ImageIcon clicAqui = new ImageIcon("C:\\direccion\\imagen.jpg");
        boton2.setIcon(new ImageIcon(clicAqui.getImage().getScaledInstance(boton2.getWidth(), boton2.getHeight(), Image.SCALE_SMOOTH)));
        boton2.setBackground(Color.BLUE);
        panel.add(boton2);

        //Botón 3 - boton de bordes/radiobotones/botón de opciones
        JButton boton3 = new JButton();
        boton3.setBounds(100,200,100,40);
        boton3.setBorder(BorderFactory.createLineBorder(Color.BLUE, 4, false));

        panel.add(boton3);


    }

    private void colocarRadioBotones(){
        JRadioButton radioBoton1 = new JRadioButton("Opción 1", true);
        radioBoton1.setBounds(50,100,200,50);
        radioBoton1.setEnabled(false);
        radioBoton1.setText("Programación");
        radioBoton1.setFont(new Font("cooper black", 0,20));
        panel.add(radioBoton1);

        JRadioButton radioBoton2 = new JRadioButton("Opción 2", false);
        radioBoton2.setBounds(50,150,100,50);
        panel.add(radioBoton2);

        JRadioButton radioBoton3 = new JRadioButton("Opción 1", false);
        radioBoton3.setBounds(50,100,100,50);
        panel.add(radioBoton3);

        ButtonGroup grupoRadioBotones = new ButtonGroup();
        grupoRadioBotones.add(radioBoton1);
        grupoRadioBotones.add(radioBoton2);
        grupoRadioBotones.add(radioBoton3);

    }

    private void colocarCajasDeTexto(){
        JTextField cajaTexto = new JTextField();
        cajaTexto.setBounds(50,50,100,30);
        cajaTexto.setText("hola");

        System.out.println("Texto en la caja: "+cajaTexto.getText());
        panel.add(cajaTexto);
    }

    private void colocarAreasDeTexto(){
        JTextArea areaTexto = new JTextArea();
        areaTexto.setBounds(20,20,300,200);
        areaTexto.setText("Escribe aquí....");
        areaTexto.append("Escribe por aquí"); //Añade mas texto al area
        areaTexto.setEditable(true); //editar el area de texto

        System.out.println("El texto es: "+areaTexto.getText());
        panel.add(areaTexto);
    }

    private void colocarListasDesplegables(){
        String [] paises = {"Perú","Colombia","Chile"};
        JComboBox listaDesplegable = new JComboBox(paises);
        listaDesplegable.setBounds(20,20,100,30);

        listaDesplegable.addItem("Argentina"); //Añadir objetos a la lista
        listaDesplegable.setSelectedItem("Chile"); //Seleccionar el primer objeto visto
        panel.add(listaDesplegable);
    }

}
