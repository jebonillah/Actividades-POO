import tkinter as tk
from tkinter import messagebox

class Empleado:
    def __init__(self, nombre, salario_por_hora, horas_trabajadas):
        self.nombre = nombre
        self.salario_por_hora = salario_por_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario_mensual(self):
        return self.salario_por_hora * self.horas_trabajadas

class InterfazEmpleado:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Salario del Empleado")
        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self.root, text="Nombre del empleado:").pack()
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.pack()
        tk.Label(self.root, text="Salario por hora:").pack()
        self.entry_salario = tk.Entry(self.root)
        self.entry_salario.pack()
        tk.Label(self.root, text="Horas trabajadas en el mes:").pack()
        self.entry_horas = tk.Entry(self.root)
        self.entry_horas.pack()
        tk.Button(self.root, text="Calcular Salario", command=self.calcular_salario).pack()

    def calcular_salario(self):
        try:
            nombre = self.entry_nombre.get()
            salario_por_hora = float(self.entry_salario.get())
            horas_trabajadas = float(self.entry_horas.get())
            empleado = Empleado(nombre, salario_por_hora, horas_trabajadas)
            salario_mensual = empleado.calcular_salario_mensual()
            if salario_mensual > 450000:
                messagebox.showinfo("Resultado", f"Nombre: {nombre}\nSalario mensual: {salario_mensual}")
            else:
                messagebox.showinfo("Resultado", f"Nombre: {nombre}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para el salario y las horas.")

    def ejecutar(self):
        self.root.mainloop()

interfaz = InterfazEmpleado()
interfaz.ejecutar()
