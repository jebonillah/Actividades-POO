import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;

public class GestionAmigosGUI extends JFrame {
    private JTextField nombreField, numeroField;
    private JTextArea areaContactos;
    private JButton btnCrear, btnMostrar, btnActualizar, btnEliminar;

    public GestionAmigosGUI() {
        setTitle("Gestión de Amigos");
        setSize(525, 460);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new FlowLayout());
        
        nombreField = new JTextField(40);
        numeroField = new JTextField(40);
        areaContactos = new JTextArea(20, 40);
        areaContactos.setEditable(false);

        btnCrear = new JButton("Crear Amigo");
        btnMostrar = new JButton("Mostrar Amigos");
        btnActualizar = new JButton("Actualizar Amigo");
        btnEliminar = new JButton("Eliminar Amigo");
        
        add(new JLabel("Nombre:"));
        add(nombreField);
        add(new JLabel("Número:"));
        add(numeroField);
        add(btnCrear);
        add(btnMostrar);
        add(btnActualizar);
        add(btnEliminar);
        add(new JScrollPane(areaContactos));

        btnCrear.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                crearContacto();
            }
        });

        btnMostrar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                mostrarContactos();
            }
        });

        btnActualizar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                actualizarContacto();
            }
        });

        btnEliminar.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                eliminarContacto();
            }
        });
    }

    private void crearContacto() {
        String nombre = nombreField.getText();
        String numeroStr = numeroField.getText();

        if (nombre.isEmpty() || numeroStr.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Por favor, complete los campos.");
            return;
        }

        try {
            long numero = Long.parseLong(numeroStr);
            File archivoContactos = new File("friendsContact.txt");

            if (!archivoContactos.exists()) {
                archivoContactos.createNewFile();
            }

            try (RandomAccessFile raf = new RandomAccessFile(archivoContactos, "rw")) {
                String linea;
                boolean encontrado = false;

                while (raf.getFilePointer() < raf.length()) {
                    linea = raf.readLine();
                    String[] partes = linea.split("!");

                    if (partes[0].equals(nombre)) {
                        encontrado = true;
                        break;
                    }
                }

                if (!encontrado) {
                    raf.writeBytes(nombre + "!" + numero + System.lineSeparator());
                    JOptionPane.showMessageDialog(this, "Contacto creado.");
                } else {
                    JOptionPane.showMessageDialog(this, "El contacto ya existe.");
                }
            }
            
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "Formato de número inválido.");
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "Error de IO: " + e.getMessage());
        }
    }
    
    private void mostrarContactos() {
        areaContactos.setText("");
        File archivoContactos = new File("friendsContact.txt");
    
        if (!archivoContactos.exists()) {
            JOptionPane.showMessageDialog(this, "No hay contactos para mostrar.");
            return;
        }
    
        StringBuilder contactos = new StringBuilder();
    
        try (RandomAccessFile raf = new RandomAccessFile(archivoContactos, "r")) {
            String linea;
    
            while (raf.getFilePointer() < raf.length()) {
                linea = raf.readLine();
    
                if (linea == null || linea.trim().isEmpty()) {
                    continue;
                }
    
                String[] partes = linea.split("!");
    
                if (partes.length == 2) {
                    contactos.append("Nombre: ").append(partes[0])
                            .append(", Número: ").append(partes[1])
                            .append("\n");
                }
            }
    
            if (contactos.length() > 0) {
                areaContactos.append(contactos.toString());
            } else {
                JOptionPane.showMessageDialog(this, "No hay contactos disponibles.");
            }
    
        } catch (IOException ex) {
            JOptionPane.showMessageDialog(this, "Error de IO: " + ex.getMessage());
        }
    }

    private void actualizarContacto() {
        String nombre = nombreField.getText();
        String numeroStr = numeroField.getText();
    
        if (nombre.isEmpty() || numeroStr.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Por favor, complete los campos.");
            return;
        }
    
        try {
            long numero = Long.parseLong(numeroStr);
            File archivoContactos = new File("friendsContact.txt");
    
            if (!archivoContactos.exists()) {
                JOptionPane.showMessageDialog(this, "No hay contactos para actualizar.");
                return;
            }
    
            File archivoTemporal = new File("temp.txt");
    
            try (RandomAccessFile raf = new RandomAccessFile(archivoContactos, "rw");
                RandomAccessFile tmpraf = new RandomAccessFile(archivoTemporal, "rw")) {
                String linea;
                boolean encontrado = false;
    
                while (raf.getFilePointer() < raf.length()) {
                    linea = raf.readLine();
                    String[] partes = linea.split("!");
    
                    if (partes.length == 2 && partes[0].equals(nombre)) {
                        encontrado = true;
                        linea = nombre + "!" + numero;
                    }
    
                    tmpraf.writeBytes(linea + System.lineSeparator());
                }
    
                if (encontrado) {
                    raf.setLength(0);
                    tmpraf.seek(0); 
    
                    while (tmpraf.getFilePointer() < tmpraf.length()) {
                        raf.writeBytes(tmpraf.readLine() + System.lineSeparator());
                    }
    
                    JOptionPane.showMessageDialog(this, "Contacto actualizado.");
                } else {
                    JOptionPane.showMessageDialog(this, "Contacto no encontrado.");
                }
    
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(this, "Error de IO: " + ex.getMessage());
            } finally {

                if (archivoTemporal.exists()) {
                    archivoTemporal.delete();
                }
            }
    
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "Formato de número inválido.");
        }
    }

    private void eliminarContacto() {
        String nameToDelete = nombreField.getText();
    
        if (nameToDelete.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Por favor, ingrese un nombre.");
            return;
        }
    
        File archivoContactos = new File("friendsContact.txt");
        if (!archivoContactos.exists()) {
            JOptionPane.showMessageDialog(this, "No hay contactos para eliminar.");
            return;
        }
    
        File archivoTemporal = new File("temp.txt");
    
        try (RandomAccessFile raf = new RandomAccessFile(archivoContactos, "rw");
            RandomAccessFile tempRaf = new RandomAccessFile(archivoTemporal, "rw")) {
            String linea;
            boolean found = false;
    
            while ((linea = raf.readLine()) != null) {
                if (linea.trim().isEmpty()) {
                    continue;
                }
    
                String[] partes = linea.split("!");
    
                if (partes.length > 0 && partes[0].equals(nameToDelete)) {
                    found = true;
                    continue;
                }
    
                tempRaf.writeBytes(linea + System.lineSeparator());
            }
    
            if (found) {
                
                raf.setLength(0);
                tempRaf.seek(0);
    
                while ((linea = tempRaf.readLine()) != null) {
                    raf.writeBytes(linea + System.lineSeparator());
                }
    
                JOptionPane.showMessageDialog(this, "Contacto eliminado.");
            } else {
                JOptionPane.showMessageDialog(this, "El contacto no fue encontrado.");
            }
    
        } catch (IOException ex) {
            JOptionPane.showMessageDialog(this, "Error: " + ex.getMessage());
        } finally {
            if (archivoTemporal.exists()) {
                archivoTemporal.delete();
            }
        }
    }
}
