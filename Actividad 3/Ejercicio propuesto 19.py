import tkinter as tk
from tkinter import messagebox
import math

class TrianguloEquilatero:
    def __init__(self, lado):
        self.lado = lado

    def calcular_perimetro(self):
        return 3 * self.lado

    def calcular_altura(self):
        return (math.sqrt(3) / 2) * self.lado

    def calcular_area(self):
        return (self.lado ** 2) * (math.sqrt(3) / 4)

class InterfazTriangulo:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Triángulo Equilátero")
        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self.root, text="Ingrese el lado del triángulo:").pack()
        self.entry_lado = tk.Entry(self.root)
        self.entry_lado.pack()
        tk.Button(self.root, text="Calcular", command=self.calcular).pack()

    def calcular(self):
        try:
            lado = float(self.entry_lado.get())
            triangulo = TrianguloEquilatero(lado)
            perimetro = triangulo.calcular_perimetro()
            altura = triangulo.calcular_altura()
            area = triangulo.calcular_area()
            messagebox.showinfo("Resultados", 
                                f"Perímetro: {perimetro}\nAltura: {altura}\nÁrea: {area}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido.")

    def ejecutar(self):
        self.root.mainloop()

interfaz = InterfazTriangulo()
interfaz.ejecutar()
