import tkinter as tk
from tkinter import messagebox

class Estudiante:
    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato):
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato = estrato

    def calcular_pago_matricula(self):
        valor_base = 50000
        if self.patrimonio > 2000000 and self.estrato > 3:
            recargo = self.patrimonio * 0.03
            return valor_base + recargo
        return valor_base

class InterfazGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Liquidación de Matrícula Universitaria")

        # Etiquetas y campos de entrada
        tk.Label(root, text="Número de Inscripción:").grid(row=0, column=0, padx=10, pady=5)
        self.inscripcion_entry = tk.Entry(root)
        self.inscripcion_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Nombres:").grid(row=1, column=0, padx=10, pady=5)
        self.nombres_entry = tk.Entry(root)
        self.nombres_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Patrimonio:").grid(row=2, column=0, padx=10, pady=5)
        self.patrimonio_entry = tk.Entry(root)
        self.patrimonio_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Estrato Social:").grid(row=3, column=0, padx=10, pady=5)
        self.estrato_entry = tk.Entry(root)
        self.estrato_entry.grid(row=3, column=1, padx=10, pady=5)

        # Botón para calcular
        tk.Button(root, text="Calcular Matrícula", command=self.calcular_matricula).grid(row=4, column=0, columnspan=2, pady=10)

    def calcular_matricula(self):
        try:
            numero_inscripcion = self.inscripcion_entry.get()
            nombres = self.nombres_entry.get()
            patrimonio = float(self.patrimonio_entry.get())
            estrato = int(self.estrato_entry.get())

            # Crear instancia de Estudiante
            estudiante = Estudiante(numero_inscripcion, nombres, patrimonio, estrato)

            # Calcular matrícula
            pago_matricula = estudiante.calcular_pago_matricula()

            # Mostrar resultados
            messagebox.showinfo("Resultados", f"Número de Inscripción: {estudiante.numero_inscripcion}\n"
                                              f"Nombres: {estudiante.nombres}\n"
                                              f"Pago de Matrícula: ${pago_matricula:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos en todos los campos.")

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazGrafica(root)
    root.mainloop()
