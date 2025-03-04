package actividad.pkg6;

import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;

public class ActualizarAmigo {
    public static void main(String data[]) {
        if (data.length < 2) {
            System.out.println("Por favor, proporciona un nombre y un número.");
            return;
        }

        try {
            String nombreNuevo = data[0];
            long numeroNuevo = Long.parseLong(data[1]);
            File archivoContactos = new File("friendsContact.txt");

            if (!archivoContactos.exists()) {
                if (archivoContactos.createNewFile()) {
                    System.out.println("Archivo creado: " + archivoContactos.getName());
                } else {
                    System.out.println("El archivo ya existe.");
                }
            }

            try (RandomAccessFile raf = new RandomAccessFile(archivoContactos, "rw")) {
                String lineaNombreNumero;
                boolean encontrado = false;

                while (raf.getFilePointer() < raf.length()) {
                    lineaNombreNumero = raf.readLine();

                    if (lineaNombreNumero == null) {
                        continue;
                    }

                    String[] partes = lineaNombreNumero.split("!");

                    if (partes.length < 2) {
                        System.out.println("Formato inválido en línea: " + lineaNombreNumero);
                        continue;
                    }

                    String nombre = partes[0];
                    long numero;

                    try {
                        numero = Long.parseLong(partes[1]);
                    } catch (NumberFormatException e) {
                        System.out.println("Número inválido en línea: " + lineaNombreNumero);
                        continue;
                    }

                    if (nombre.equals(nombreNuevo) || numero == numeroNuevo) {
                        encontrado = true;
                        break;
                    }
                }

                if (encontrado) {
                    File archivoTemporal = new File("temp.txt");

                    try (RandomAccessFile tmpraf = new RandomAccessFile(archivoTemporal, "rw")) {
                        raf.seek(0);

                        while (raf.getFilePointer() < raf.length()) {
                            lineaNombreNumero = raf.readLine();

                            String[] partes = lineaNombreNumero.split("!");
                            String nombre = partes[0];

                            if (nombre.equals(nombreNuevo)) {
                                lineaNombreNumero = nombre + "!" + numeroNuevo;
                            }

                            tmpraf.writeBytes(lineaNombreNumero);
                            tmpraf.writeBytes(System.lineSeparator());
                        }

                        raf.seek(0);
                        tmpraf.seek(0);

                        while (tmpraf.getFilePointer() < tmpraf.length()) {
                            raf.writeBytes(tmpraf.readLine());
                            raf.writeBytes(System.lineSeparator());
                        }
                        
                        raf.setLength(tmpraf.length());
                    }

                    archivoTemporal.delete();
                    System.out.println("Amigo actualizado.");
                } else {
                    System.out.println("El nombre ingresado no existe.");
                }
            }
        } catch (IOException ioe) {
            System.out.println("Error de IO: " + ioe.getMessage());
        } catch (NumberFormatException nef) {
            System.out.println("Formato de número inválido: " + nef.getMessage());
        }
    }
}