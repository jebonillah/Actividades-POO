import tkinter as tk
from tkinter import messagebox

# Clase Empleado
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

# Función para calcular y mostrar los resultados
def calcular_salarios():
    try:
        codigo = entry_codigo.get()
        nombres = entry_nombres.get()
        horas_trabajadas = float(entry_horas.get())
        valor_hora = float(entry_valor_hora.get())
        porcentaje_retencion = float(entry_retencion.get())

        empleado = Empleado(codigo, nombres, horas_trabajadas, valor_hora, porcentaje_retencion)
        salario_bruto = empleado.calcular_salario_bruto()
        salario_neto = empleado.calcular_salario_neto()

        messagebox.showinfo("Resultados", f"Código: {codigo}\nNombres: {nombres}\nSalario Bruto: ${salario_bruto:.2f}\nSalario Neto: ${salario_neto:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora de Salarios")

tk.Label(root, text="Código del Empleado").grid(row=0, column=0)
entry_codigo = tk.Entry(root)
entry_codigo.grid(row=0, column=1)

tk.Label(root, text="Nombres").grid(row=1, column=0)
entry_nombres = tk.Entry(root)
entry_nombres.grid(row=1, column=1)

tk.Label(root, text="Horas Trabajadas").grid(row=2, column=0)
entry_horas = tk.Entry(root)
entry_horas.grid(row=2, column=1)

tk.Label(root, text="Valor por Hora").grid(row=3, column=0)
entry_valor_hora = tk.Entry(root)
entry_valor_hora.grid(row=3, column=1)

tk.Label(root, text="Porcentaje de Retención").grid(row=4, column=0)
entry_retencion = tk.Entry(root)
entry_retencion.grid(row=4, column=1)

tk.Button(root, text="Calcular Salarios", command=calcular_salarios).grid(row=5, column=0, columnspan=2)

root.mainloop()
