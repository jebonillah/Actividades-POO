import tkinter as tk
from tkinter import messagebox
import math

class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_soluciones(self):
        discriminante = self.b ** 2 - 4 * self.a * self.c
        if discriminante < 0:
            return "No hay soluciones reales"
        elif discriminante == 0:
            solucion = -self.b / (2 * self.a)
            return f"Una solución real: {solucion}"
        else:
            raiz1 = (-self.b + math.sqrt(discriminante)) / (2 * self.a)
            raiz2 = (-self.b - math.sqrt(discriminante)) / (2 * self.a)
            return f"Dos soluciones reales: {raiz1}, {raiz2}"

class InterfazEcuacionCuadratica:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ecuación Cuadrática")
        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self.root, text="Ingrese el valor de A:").pack()
        self.entry_a = tk.Entry(self.root)
        self.entry_a.pack()
        tk.Label(self.root, text="Ingrese el valor de B:").pack()
        self.entry_b = tk.Entry(self.root)
        self.entry_b.pack()
        tk.Label(self.root, text="Ingrese el valor de C:").pack()
        self.entry_c = tk.Entry(self.root)
        self.entry_c.pack()
        tk.Button(self.root, text="Calcular Soluciones", command=self.calcular_soluciones).pack()

    def calcular_soluciones(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            c = float(self.entry_c.get())
            ecuacion = EcuacionCuadratica(a, b, c)
            soluciones = ecuacion.calcular_soluciones()
            messagebox.showinfo("Soluciones", soluciones)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para A, B y C.")

    def ejecutar(self):
        self.root.mainloop()

interfaz = InterfazEcuacionCuadratica()
interfaz.ejecutar()
