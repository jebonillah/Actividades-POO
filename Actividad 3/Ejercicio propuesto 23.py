import tkinter as tk
from tkinter import messagebox
import cmath

# Clase EcuacionCuadratica
class EcuacionCuadratica:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular_soluciones(self):
        discriminante = cmath.sqrt(self.b**2 - 4*self.a*self.c)
        solucion1 = (-self.b + discriminante) / (2 * self.a)
        solucion2 = (-self.b - discriminante) / (2 * self.a)
        return solucion1, solucion2

# Función para calcular y mostrar las soluciones
def calcular_ecuacion():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a == 0:
            messagebox.showerror("Error", "El coeficiente A no puede ser cero.")
            return

        ecuacion = EcuacionCuadratica(a, b, c)
        solucion1, solucion2 = ecuacion.calcular_soluciones()

        messagebox.showinfo("Soluciones", f"Solución 1: {solucion1}\nSolución 2: {solucion2}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora de Ecuación Cuadrática")

tk.Label(root, text="Valor de A").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="Valor de B").grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

tk.Label(root, text="Valor de C").grid(row=2, column=0)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1)

tk.Button(root, text="Calcular Soluciones", command=calcular_ecuacion).grid(row=3, column=0, columnspan=2)

root.mainloop()
