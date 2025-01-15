import tkinter as tk

class Empleado:
    def __init__(self, codigo, nombres, horas_trabajadas, valor_hora, retencion):
        self.codigo = codigo
        self.nombres = nombres
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora
        self.retencion = retencion

    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.valor_hora

    def calcular_salario_neto(self):
        salario_bruto = self.calcular_salario_bruto()
        return salario_bruto * (1 - self.retencion / 100)

class InterfazEmpleado:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Empleado")

        # Widgets de entrada
        tk.Label(self.root, text="Código").grid(row=0, column=0)
        tk.Label(self.root, text="Nombres").grid(row=1, column=0)
        tk.Label(self.root, text="Horas Trabajadas").grid(row=2, column=0)
        tk.Label(self.root, text="Valor por Hora").grid(row=3, column=0)
        tk.Label(self.root, text="Retención (%)").grid(row=4, column=0)

        self.codigo = tk.Entry(self.root)
        self.nombres = tk.Entry(self.root)
        self.horas_trabajadas = tk.Entry(self.root)
        self.valor_hora = tk.Entry(self.root)
        self.retencion = tk.Entry(self.root)

        self.codigo.grid(row=0, column=1)
        self.nombres.grid(row=1, column=1)
        self.horas_trabajadas.grid(row=2, column=1)
        self.valor_hora.grid(row=3, column=1)
        self.retencion.grid(row=4, column=1)

        # Botón
        tk.Button(self.root, text="Calcular", command=self.calcular).grid(row=5, columnspan=2)

        # Resultados
        self.resultado = tk.Text(self.root, height=5, width=30)
        self.resultado.grid(row=6, columnspan=2)

    def calcular(self):
        emp = Empleado(
            self.codigo.get(),
            self.nombres.get(),
            float(self.horas_trabajadas.get()),
            float(self.valor_hora.get()),
            float(self.retencion.get())
        )

        salario_bruto = emp.calcular_salario_bruto()
        salario_neto = emp.calcular_salario_neto()

        resultado_texto = (
            f"Código: {emp.codigo}\n"
            f"Nombres: {emp.nombres}\n"
            f"Salario Bruto: {salario_bruto}\n"
            f"Salario Neto: {salario_neto}\n"
        )

        self.resultado.delete(1.0, tk.END)
        self.resultado.insert(tk.END, resultado_texto)

    def ejecutar(self):
        self.root.mainloop()

# InterfazEmpleado().ejecutar()
