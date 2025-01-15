import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, retencion):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.retencion = retencion

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto * (1 - self.retencion / 100)

class InterfazEmpleado:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Empleado")
        self.crear_interfaz()

    def crear_interfaz(self):
        # Widgets de entrada
        tk.Label(self.root, text="Código").grid(row=0, column=0)
        tk.Label(self.root, text="Nombres").grid(row=1, column=0)
        tk.Label(self.root, text="Horas Trabajadas").grid(row=2, column=0)
        tk.Label(self.root, text="Valor por Hora").grid(row=3, column=0)
        tk.Label(self.root, text="Retención (%)").grid(row=4, column=0)

        self.codigo_entry = tk.Entry(self.root)
        self.nombres_entry = tk.Entry(self.root)
        self.horas_trabajadas_entry = tk.Entry(self.root)
        self.valor_hora_entry = tk.Entry(self.root)
        self.retencion_entry = tk.Entry(self.root)

        self.codigo_entry.grid(row=0, column=1)
        self.nombres_entry.grid(row=1, column=1)
        self.horas_trabajadas_entry.grid(row=2, column=1)
        self.valor_hora_entry.grid(row=3, column=1)
        self.retencion_entry.grid(row=4, column=1)

        # Botón
        tk.Button(self.root, text="Calcular", command=self.calcular).grid(row=5, columnspan=2)

    def calcular(self):
        try:
            codigo = self.codigo_entry.get()
            nombres = self.nombres_entry.get()
            horas_trabajadas = float(self.horas_trabajadas_entry.get())
            valor_hora = float(self.valor_hora_entry.get())
            retencion = float(self.retencion_entry.get())

            empleado = Empleado(codigo, nombres, horas_trabajadas, valor_hora, retencion)

            salario_bruto = empleado.calcular_salario_bruto()
            salario_neto = empleado.calcular_salario_neto()

            resultado_texto = (
                f"Código: {empleado.codigo}\n"
                f"Nombres: {empleado.nombres}\n"
                f"Salario Bruto: {salario_bruto:.2f}\n"
                f"Salario Neto: {salario_neto:.2f}\n"
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
interfaz = InterfazEmpleado()
interfaz.ejecutar()
