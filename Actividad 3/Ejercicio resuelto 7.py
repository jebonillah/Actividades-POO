import tkinter as tk
from tkinter import messagebox

# Clase Comparador
class Comparador:
    @staticmethod
    def comparar(a, b):
        if a > b:
            return "A es mayor que B."
        elif a < b:
            return "A es menor que B."
        else:
            return "A es igual a B."

# Función para realizar la comparación y mostrar el resultado
def comparar_valores():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        resultado = Comparador.comparar(a, b)
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Comparador de Valores")

tk.Label(root, text="Valor A").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="Valor B").grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

tk.Button(root, text="Comparar", command=comparar_valores).grid(row=2, column=0, columnspan=2)

root.mainloop()
