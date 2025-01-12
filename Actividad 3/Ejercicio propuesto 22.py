import tkinter as tk
from tkinter import messagebox

# Clase Empleado
class Empleado:
    def __init__(self, nombre, salario_basico_por_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_basico_por_hora = salario_basico_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_basico_por_hora * self.horas_trabajadas

# Función para calcular y mostrar el salario mensual
def calcular_salario():
    try:
        nombre = entry_nombre.get()
        salario_basico_por_hora = float(entry_salario_hora.get())
        horas_trabajadas = float(entry_horas.get())

        empleado = Empleado(nombre, salario_basico_por_hora, horas_trabajadas)
        salario_mensual = empleado.calcular_salario_mensual()

        if salario_mensual > 450000:
            messagebox.showinfo("Resultado", f"Nombre: {nombre}\nSalario Mensual: ${salario_mensual:.2f}")
        else:
            messagebox.showinfo("Resultado", f"Nombre: {nombre}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos para salario y horas trabajadas.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora de Salario Mensual")

tk.Label(root, text="Nombre del Empleado").grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Salario Básico por Hora").grid(row=1, column=0)
entry_salario_hora = tk.Entry(root)
entry_salario_hora.grid(row=1, column=1)

tk.Label(root, text="Horas Trabajadas en el Mes").grid(row=2, column=0)
entry_horas = tk.Entry(root)
entry_horas.grid(row=2, column=1)

tk.Button(root, text="Calcular Salario", command=calcular_salario).grid(row=3, column=0, columnspan=2)

root.mainloop()
