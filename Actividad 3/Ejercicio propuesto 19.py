import tkinter as tk
from tkinter import messagebox
import math

# Clase TrianguloEquilatero
class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        return 3 * self.lado

    def calcular_altura(self):
        return (math.sqrt(3) / 2) * self.lado

    def calcular_area(self):
        return (self.lado * self.calcular_altura()) / 2

# Función para calcular y mostrar los resultados
def calcular_triangulo():
    try:
        lado = float(entry_lado.get())

        triangulo = TrianguloEquilatero(lado)
        perimetro = triangulo.calcular_perimetro()
        altura = triangulo.calcular_altura()
        area = triangulo.calcular_area()

        messagebox.showinfo("Resultados", f"Lado: {lado}\nPerímetro: {perimetro:.2f}\nAltura: {altura:.2f}\nÁrea: {area:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un valor válido para el lado.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora de Triángulo Equilátero")

tk.Label(root, text="Valor del Lado").grid(row=0, column=0)
entry_lado = tk.Entry(root)
entry_lado.grid(row=0, column=1)

tk.Button(root, text="Calcular", command=calcular_triangulo).grid(row=1, column=0, columnspan=2)

root.mainloop()
