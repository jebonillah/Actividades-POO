package actividad.pkg6;

import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;

public class AgregarAmigo {
    public static void main(String data[]) {
        if (data.length < 2) {
            System.out.println("Por favor, proporciona un nombre y un número.");
            return;
        }

        try {
            String nuevoNombre = data[0];
            long nuevoNumero = Long.parseLong(data[1]);
            File archivoContactos = new File("friendsContact.txt");

            if (!archivoContactos.exists()) {
                if (archivoContactos.createNewFile()) {
                    System.out.println("Archivo creado: " + archivoContactos.getName());
                } else {
                    System.out.println("El archivo ya existe.");
                }
            }

            try (RandomAccessFile raf = new RandomAccessFile(archivoContactos, "rw")) {
                String nombreNumeroString;
                boolean found = false;

                while (raf.getFilePointer() < raf.length()) {
                    nombreNumeroString = raf.readLine();
                    if (nombreNumeroString == null) {
                        continue; 
                    }

                    String[] lineSplit = nombreNumeroString.split("!");
                    if (lineSplit.length < 2) {
                        System.out.println("Formato inválido en línea: " + nombreNumeroString);
                        continue;
                    }

                    String nombre = lineSplit[0];
                    long numero;

                    try {
                        numero = Long.parseLong(lineSplit[1]);
                    } catch (NumberFormatException e) {
                        System.out.println("Número inválido en línea: " + nombreNumeroString);
                        continue;
                    }

                    if (nombre.equals(nuevoNombre) || numero == nuevoNumero) {
                        found = true;
                        break;
                    }
                }

                if (!found) {
                    nombreNumeroString = nuevoNombre + "!" + nuevoNumero;
                    raf.writeBytes(nombreNumeroString);
                    raf.writeBytes(System.lineSeparator());
                    System.out.println("Amigo agregado.");
                } else {
                    System.out.println("El nombre o numero ya existe.");
                }
            }
        } catch (IOException ioe) {
            System.out.println("Error de IO: " + ioe.getMessage());
        } catch (NumberFormatException nef) {
            System.out.println("Formato de numero invalido: " + nef.getMessage());
        }
    }
}