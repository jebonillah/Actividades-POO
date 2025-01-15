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
            valor_base += self.patrimonio * 0.03
        return valor_base

class InterfazEstudiante:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Liquidación de Matrícula")
        self.crear_interfaz()

    def crear_interfaz(self):
        # Widgets de entrada
        tk.Label(self.root, text="Número de Inscripción").grid(row=0, column=0)
        tk.Label(self.root, text="Nombres").grid(row=1, column=0)
        tk.Label(self.root, text="Patrimonio").grid(row=2, column=0)
        tk.Label(self.root, text="Estrato Social").grid(row=3, column=0)

        self.numero_inscripcion_entry = tk.Entry(self.root)
        self.nombres_entry = tk.Entry(self.root)
        self.patrimonio_entry = tk.Entry(self.root)
        self.estrato_entry = tk.Entry(self.root)

        self.numero_inscripcion_entry.grid(row=0, column=1)
        self.nombres_entry.grid(row=1, column=1)
        self.patrimonio_entry.grid(row=2, column=1)
        self.estrato_entry.grid(row=3, column=1)

        # Botón
        tk.Button(self.root, text="Calcular", command=self.calcular).grid(row=4, columnspan=2)

    def calcular(self):
        try:
            numero_inscripcion = self.numero_inscripcion_entry.get()
            nombres = self.nombres_entry.get()
            patrimonio = float(self.patrimonio_entry.get())
            estrato = int(self.estrato_entry.get())

            estudiante = Estudiante(numero_inscripcion, nombres, patrimonio, estrato)

            pago_matricula = estudiante.calcular_pago_matricula()

            resultado_texto = (
                f"Número de Inscripción: {estudiante.numero_inscripcion}\n"
                f"Nombres: {estudiante.nombres}\n"
                f"Pago de Matrícula: {pago_matricula:.2f}\n"
            )

            self.mostrar_resultado(resultado_texto)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

    def mostrar_resultado(self, resultado_texto):
        resultado_ventana = tk.Toplevel(self.root)
        resultado_ventana.title("Resultado")
        tk.Label(resultado_ventana, text=resultado_texto, justify="left").pack(padx=10, pady=10)
        tk.Button(resultado_ventana, text="Cerrar", command=resultado_ventana.destroy).pack(pady=10)

    def ejecutar(self):
        self.root.mainloop()

# Para ejecutar la interfaz:
interfaz = InterfazEstudiante()
interfaz.ejecutar()
