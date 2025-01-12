import tkinter as tk
from tkinter import messagebox

# Clase Estudiante
class Estudiante:
    def __init__(self, numero_inscripcion, nombres, patrimonio, estrato_social):
        self.numero_inscripcion = numero_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato_social = estrato_social
        self.pago_base = 50000

    def calcular_pago_matricula(self):
        if self.patrimonio > 2000000 and self.estrato_social > 3:
            incremento = self.patrimonio * 0.03
        else:
            incremento = 0
        return self.pago_base + incremento

# Función para calcular y mostrar el pago de matrícula
def calcular_matricula():
    try:
        numero_inscripcion = entry_numero.get()
        nombres = entry_nombres.get()
        patrimonio = float(entry_patrimonio.get())
        estrato_social = int(entry_estrato.get())

        estudiante = Estudiante(numero_inscripcion, nombres, patrimonio, estrato_social)
        pago_matricula = estudiante.calcular_pago_matricula()

        messagebox.showinfo("Resultado", f"Número de Inscripción: {numero_inscripcion}\nNombres: {nombres}\nPago de Matrícula: ${pago_matricula:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos para patrimonio y estrato social.")

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Calculadora de Pago de Matrícula")

tk.Label(root, text="Número de Inscripción").grid(row=0, column=0)
entry_numero = tk.Entry(root)
entry_numero.grid(row=0, column=1)

tk.Label(root, text="Nombres").grid(row=1, column=0)
entry_nombres = tk.Entry(root)
entry_nombres.grid(row=1, column=1)

tk.Label(root, text="Patrimonio").grid(row=2, column=0)
entry_patrimonio = tk.Entry(root)
entry_patrimonio.grid(row=2, column=1)

tk.Label(root, text="Estrato Social").grid(row=3, column=0)
entry_estrato = tk.Entry(root)
entry_estrato.grid(row=3, column=1)

tk.Button(root, text="Calcular Matrícula", command=calcular_matricula).grid(row=4, column=0, columnspan=2)

root.mainloop()
