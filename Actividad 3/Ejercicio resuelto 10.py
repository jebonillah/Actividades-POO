import tkinter as tk

class Estudiante:
    def __init__(self, num_inscripcion, nombres, patrimonio, estrato):
        self.num_inscripcion = num_inscripcion
        self.nombres = nombres
        self.patrimonio = patrimonio
        self.estrato = estrato

    def calcular_pago_matricula(self):
        base_pago = 50000
        if self.patrimonio > 2000000 and self.estrato > 3:
            return base_pago + (self.patrimonio * 0.03)
        return base_pago

class InterfazEstudiante:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Estudiante")

        # Widgets de entrada
        tk.Label(self.root, text="Número de Inscripción").grid(row=0, column=0)
        tk.Label(self.root, text="Nombres").grid(row=1, column=0)
        tk.Label(self.root, text="Patrimonio").grid(row=2, column=0)
        tk.Label(self.root, text="Estrato").grid(row=3, column=0)

        self.num_inscripcion = tk.Entry(self.root)
        self.nombres = tk.Entry(self.root)
        self.patrimonio = tk.Entry(self.root)
        self.estrato = tk.Entry(self.root)

        self.num_inscripcion.grid(row=0, column=1)
        self.nombres.grid(row=1, column=1)
        self.patrimonio.grid(row=2, column=1)
        self.estrato.grid(row=3, column=1)

        # Botón
        tk.Button(self.root, text="Calcular", command=self.calcular).grid(row=4, columnspan=2)

        # Resultados
        self.resultado = tk.Text(self.root, height=5, width=30)
        self.resultado.grid(row=5, columnspan=2)

    def calcular(self):
        est = Estudiante(
            self.num_inscripcion.get(),
            self.nombres.get(),
            float(self.patrimonio.get()),
            int(self.estrato.get())
        )

        pago_matricula = est.calcular_pago_matricula()

        resultado_texto = (
            f"Número de Inscripción: {est.num_inscripcion}\n"
            f"Nombres: {est.nombres}\n"
            f"Pago de Matrícula: {pago_matricula}\n"
        )

        self.resultado.delete(1.0, tk.END)
        self.resultado.insert(tk.END, resultado_texto)

    def ejecutar(self):
        self.root.mainloop()

# InterfazEstudiante().ejecutar()
