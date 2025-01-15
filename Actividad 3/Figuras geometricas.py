import tkinter as tk
from tkinter import messagebox
import math

# Definición de las clases para las figuras geométricas
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        return math.sqrt(self.base ** 2 + self.altura ** 2)

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo(self):
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            return "Equilátero"
        elif self.base == self.altura or self.base == hipotenusa or self.altura == hipotenusa:
            return "Isósceles"
        else:
            return "Escaleno"

# Clase para la interfaz gráfica
class InterfazFiguras:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de Figuras Geométricas")
        self.crear_interfaz()

    def crear_interfaz(self):
        # Círculo
        frame_circulo = tk.Frame(self.root)
        frame_circulo.pack(pady=10)
        tk.Label(frame_circulo, text="Círculo - Radio").pack()
        self.entry_radio = tk.Entry(frame_circulo)
        self.entry_radio.pack()
        tk.Button(frame_circulo, text="Calcular Círculo", command=self.calcular_circulo).pack()

        # Rectángulo
        frame_rectangulo = tk.Frame(self.root)
        frame_rectangulo.pack(pady=10)
        tk.Label(frame_rectangulo, text="Rectángulo - Base y Altura").pack()
        self.entry_base_rectangulo = tk.Entry(frame_rectangulo)
        self.entry_base_rectangulo.pack()
        self.entry_altura_rectangulo = tk.Entry(frame_rectangulo)
        self.entry_altura_rectangulo.pack()
        tk.Button(frame_rectangulo, text="Calcular Rectángulo", command=self.calcular_rectangulo).pack()

        # Cuadrado
        frame_cuadrado = tk.Frame(self.root)
        frame_cuadrado.pack(pady=10)
        tk.Label(frame_cuadrado, text="Cuadrado - Lado").pack()
        self.entry_lado = tk.Entry(frame_cuadrado)
        self.entry_lado.pack()
        tk.Button(frame_cuadrado, text="Calcular Cuadrado", command=self.calcular_cuadrado).pack()

        # Triángulo Rectángulo
        frame_triangulo = tk.Frame(self.root)
        frame_triangulo.pack(pady=10)
        tk.Label(frame_triangulo, text="Triángulo Rectángulo - Base y Altura").pack()
        self.entry_base_triangulo = tk.Entry(frame_triangulo)
        self.entry_base_triangulo.pack()
        self.entry_altura_triangulo = tk.Entry(frame_triangulo)
        self.entry_altura_triangulo.pack()
        tk.Button(frame_triangulo, text="Calcular Triángulo", command=self.calcular_triangulo).pack()

    def calcular_circulo(self):
        try:
            radio = float(self.entry_radio.get())
            circulo = Circulo(radio)
            area = circulo.calcular_area()
            perimetro = circulo.calcular_perimetro()
            messagebox.showinfo("Resultados Círculo", f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido para el radio.")

    def calcular_rectangulo(self):
        try:
            base = float(self.entry_base_rectangulo.get())
            altura = float(self.entry_altura_rectangulo.get())
            rectangulo = Rectangulo(base, altura)
            area = rectangulo.calcular_area()
            perimetro = rectangulo.calcular_perimetro()
            messagebox.showinfo("Resultados Rectángulo", f"Área: {area}\nPerímetro: {perimetro}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para la base y altura.")

    def calcular_cuadrado(self):
        try:
            lado = float(self.entry_lado.get())
            cuadrado = Cuadrado(lado)
            area = cuadrado.calcular_area()
            perimetro = cuadrado.calcular_perimetro()
            messagebox.showinfo("Resultados Cuadrado", f"Área: {area}\nPerímetro: {perimetro}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido para el lado.")

    def calcular_triangulo(self):
        try:
            base = float(self.entry_base_triangulo.get())
            altura = float(self.entry_altura_triangulo.get())
            triangulo = TrianguloRectangulo(base, altura)
            area = triangulo.calcular_area()
            perimetro = triangulo.calcular_perimetro()
            hipotenusa = triangulo.calcular_hipotenusa()
            tipo = triangulo.determinar_tipo()
            messagebox.showinfo("Resultados Triángulo Rectángulo", 
                                f"Área: {area}\nPerímetro: {perimetro:.2f}\nHipotenusa: {hipotenusa:.2f}\nTipo: {tipo}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para la base y altura.")

    def ejecutar(self):
        self.root.mainloop()

# Instanciar y ejecutar la interfaz gráfica
interfaz = InterfazFiguras()
interfaz.ejecutar()
