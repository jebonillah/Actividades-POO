import tkinter as tk
from tkinter import messagebox

class Comparador:
    @staticmethod
    def comparar(a, b):
        if a > b:
            return "A es mayor que B"
        elif a < b:
            return "A es menor que B"
        else:
            return "A es igual a B"

class InterfazComparador:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Comparador de Números")
        self.crear_interfaz()

    def crear_interfaz(self):
        tk.Label(self.root, text="Ingrese el valor de A:").pack()
        self.entry_a = tk.Entry(self.root)
        self.entry_a.pack()
        tk.Label(self.root, text="Ingrese el valor de B:").pack()
        self.entry_b = tk.Entry(self.root)
        self.entry_b.pack()
        tk.Button(self.root, text="Comparar", command=self.comparar).pack()

    def comparar(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            resultado = Comparador.comparar(a, b)
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    def ejecutar(self):
        self.root.mainloop()

interfaz = InterfazComparador()
interfaz.ejecutar()
