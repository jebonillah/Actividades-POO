package actividad.pkg6;

import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;

public class MostrarAmigos {
    public static void main(String data[]) {
        try {
            String lineaNombreNumero;
            String nombre;
            long numero;
            File archivoContactos = new File("friendsContact.txt");

            if (!archivoContactos.exists()) {
                if (archivoContactos.createNewFile()) {
                    System.out.println("Archivo creado: " + archivoContactos.getName());
                } else {
                    System.out.println("El archivo ya existe.");
                }
            }

            try (RandomAccessFile raf = new RandomAccessFile(archivoContactos, "rw")) {
                while (raf.getFilePointer() < raf.length()) {
                    lineaNombreNumero = raf.readLine();
                    
                    if (lineaNombreNumero == null) {
                        continue;
                    }

                    String[] partes = lineaNombreNumero.split("!");

                    if (partes.length < 2) {
                        System.out.println("Formato invalido en línea: " + lineaNombreNumero);
                        continue;
                    }

                    nombre = partes[0];
                    
                    try {
                        numero = Long.parseLong(partes[1]);
                    } catch (NumberFormatException e) {
                        System.out.println("Numero invalido en línea: " + lineaNombreNumero);
                        continue;
                    }

                    System.out.println("Nombre del Amigo: " + nombre + "\n" + "Numero de Contacto: " + numero + "\n");
                }
            }
        } catch (IOException ioe) {
            System.out.println("Error de IO: " + ioe.getMessage());
        } catch (NumberFormatException nef) {
            System.out.println("Formato de número invalido: " + nef.getMessage());
        }
    }
}