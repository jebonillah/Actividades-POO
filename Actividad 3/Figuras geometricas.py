import tkinter as tk
from tkinter import messagebox
import math

# Clase Círculo
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

# Clase Rectángulo
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

# Clase Cuadrado
class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

# Clase Triángulo Rectángulo
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

# Funciones para cada figura
def calcular_circulo():
    try:
        radio = float(entry_radio.get())
        circulo = Circulo(radio)
        area = circulo.calcular_area()
        perimetro = circulo.calcular_perimetro()
        messagebox.showinfo("Resultados Círculo", f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido para el radio.")

def calcular_rectangulo():
    try:
        base = float(entry_base_rectangulo.get())
        altura = float(entry_altura_rectangulo.get())
        rectangulo = Rectangulo(base, altura)
        area = rectangulo.calcular_area()
        perimetro = rectangulo.calcular_perimetro()
        messagebox.showinfo("Resultados Rectángulo", f"Área: {area}\nPerímetro: {perimetro}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para la base y altura.")

def calcular_cuadrado():
    try:
        lado = float(entry_lado.get())
        cuadrado = Cuadrado(lado)
        area = cuadrado.calcular_area()
        perimetro = cuadrado.calcular_perimetro()
        messagebox.showinfo("Resultados Cuadrado", f"Área: {area}\nPerímetro: {perimetro}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese un valor numérico válido para el lado.")

def calcular_triangulo():
    try:
        base = float(entry_base_triangulo.get())
        altura = float(entry_altura_triangulo.get())
        triangulo = TrianguloRectangulo(base, altura)
        area = triangulo.calcular_area()
        perimetro = triangulo.calcular_perimetro()
        hipotenusa = triangulo.calcular_hipotenusa()
        tipo = triangulo.determinar_tipo()
        messagebox.showinfo("Resultados Triángulo Rectángulo", 
                            f"Área: {area}\nPerímetro: {perimetro:.2f}\nHipotenusa: {hipotenusa:.2f}\nTipo: {tipo}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos para la base y altura.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora de Figuras Geométricas")

# Ventana para Círculo
frame_circulo = tk.Frame(root)
frame_circulo.pack(pady=10)
tk.Label(frame_circulo, text="Círculo - Radio").pack()
entry_radio = tk.Entry(frame_circulo)
entry_radio.pack()
tk.Button(frame_circulo, text="Calcular Círculo", command=calcular_circulo).pack()

# Ventana para Rectángulo
frame_rectangulo = tk.Frame(root)
frame_rectangulo.pack(pady=10)
tk.Label(frame_rectangulo, text="Rectángulo - Base y Altura").pack()
entry_base_rectangulo = tk.Entry(frame_rectangulo)
entry_base_rectangulo.pack()
entry_altura_rectangulo = tk.Entry(frame_rectangulo)
entry_altura_rectangulo.pack()
tk.Button(frame_rectangulo, text="Calcular Rectángulo", command=calcular_rectangulo).pack()

# Ventana para Cuadrado
frame_cuadrado = tk.Frame(root)
frame_cuadrado.pack(pady=10)
tk.Label(frame_cuadrado, text="Cuadrado - Lado").pack()
entry_lado = tk.Entry(frame_cuadrado)
entry_lado.pack()
tk.Button(frame_cuadrado, text="Calcular Cuadrado", command=calcular_cuadrado).pack()

# Ventana para Triángulo Rectángulo
frame_triangulo = tk.Frame(root)
frame_triangulo.pack(pady=10)
tk.Label(frame_triangulo, text="Triángulo Rectángulo - Base y Altura").pack()
entry_base_triangulo = tk.Entry(frame_triangulo)
entry_base_triangulo.pack()
entry_altura_triangulo = tk.Entry(frame_triangulo)
entry_altura_triangulo.pack()
tk.Button(frame_triangulo, text="Calcular Triángulo", command=calcular_triangulo).pack()

root.mainloop()
