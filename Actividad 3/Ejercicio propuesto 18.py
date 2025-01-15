import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, porcentaje_retencion):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.porcentaje_retencion = porcentaje_retencion

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        retencion = salario_bruto * (self.porcentaje_retencion / 100)
        return salario_bruto - retencion

class InterfazGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Nómina")

        # Etiquetas y campos de entrada
        tk.Label(root, text="Código del Empleado:").grid(row=0, column=0, padx=10, pady=5)
        self.codigo_entry = tk.Entry(root)
        self.codigo_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Nombres:").grid(row=1, column=0, padx=10, pady=5)
        self.nombres_entry = tk.Entry(root)
        self.nombres_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Horas Trabajadas al Mes:").grid(row=2, column=0, padx=10, pady=5)
        self.horas_trabajadas_entry = tk.Entry(root)
        self.horas_trabajadas_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Valor por Hora Trabajada:").grid(row=3, column=0, padx=10, pady=5)
        self.valor_hora_entry = tk.Entry(root)
        self.valor_hora_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="% Retención en la Fuente:").grid(row=4, column=0, padx=10, pady=5)
        self.retencion_entry = tk.Entry(root)
        self.retencion_entry.grid(row=4, column=1, padx=10, pady=5)

        # Botón para calcular
        tk.Button(root, text="Calcular Salarios", command=self.calcular_salarios).grid(row=5, column=0, columnspan=2, pady=10)

    def calcular_salarios(self):
        try:
            codigo = self.codigo_entry.get()
            nombres = self.nombres_entry.get()
            horas_trabajadas = float(self.horas_trabajadas_entry.get())
            valor_hora = float(self.valor_hora_entry.get())
            porcentaje_retencion = float(self.retencion_entry.get())

            # Crear instancia de Empleado
            empleado = Empleado(codigo, nombres, horas_trabajadas, valor_hora, porcentaje_retencion)

            # Cálculos
            salario_bruto = empleado.calcular_salario_bruto()
            salario_neto = empleado.calcular_salario_neto()

            # Mostrar resultados
            messagebox.showinfo("Resultados", f"Código: {empleado.codigo}\n"
                                         f"Nombres: {empleado.nombres}\n"
                                         f"Salario Bruto: ${salario_bruto:.2f}\n"
                                         f"Salario Neto: ${salario_neto:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos en todos los campos.")

# Inicializar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazGrafica(root)
    root.mainloop()
