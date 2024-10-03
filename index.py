import tkinter as tk
from tkinter import messagebox
import calc_temp as ct

def convertir_temperatura():
    try:
        valor = float(entry_valor.get())
    except ValueError:
        messagebox.showerror("Error", "Ingresa un valor numérico.")
        return

    unidad_origen = unidad_origen_var.get()
    unidad_destino = unidad_destino_var.get()

    if unidad_origen == unidad_destino:
        messagebox.showinfo("Resultado", f"El valor es el mismo: {valor} {unidad_destino}")
        return

    try:
        if unidad_origen == "Celsius":
            if unidad_destino == "Fahrenheit":
                resultado = ct.celsius_to_fahrenheit(valor)
            elif unidad_destino == "Kelvin":
                resultado = ct.celsius_to_kelvin(valor)
        elif unidad_origen == "Fahrenheit":
            if unidad_destino == "Celsius":
                resultado = ct.fahrenheit_to_celsius(valor)
            elif unidad_destino == "Kelvin":
                resultado = ct.fahrenheit_to_kelvin(valor)
        elif unidad_origen == "Kelvin":
            if valor < 0:
                messagebox.showerror("Error", "El valor en Kelvin no puede ser negativo")
                return
            if unidad_destino == "Celsius":
                resultado = ct.kelvin_to_celsius(valor)
            elif unidad_destino == "Fahrenheit":
                resultado = ct.kelvin_to_fahrenheit(valor)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    label_resultado.config(text=f"Resultado: {round(resultado, 2)} {unidad_destino}")

root = tk.Tk()
root.title("Calculadora de Temperaturas")

label_valor = tk.Label(root, text="Valor de temperatura:")
label_valor.grid(row=0, column=0, padx=10, pady=10)

entry_valor = tk.Entry(root)
entry_valor.grid(row=0, column=1, padx=10, pady=10)

unidad_origen_var = tk.StringVar(value="Celsius")
unidad_destino_var = tk.StringVar(value="Fahrenheit")

label_origen = tk.Label(root, text="Unidad origen:")
label_origen.grid(row=1, column=0, padx=10, pady=10)

combo_origen = tk.OptionMenu(root, unidad_origen_var, "Celsius", "Fahrenheit", "Kelvin")
combo_origen.grid(row=1, column=1, padx=10, pady=10)

label_destino = tk.Label(root, text="Unidad destino:")
label_destino.grid(row=2, column=0, padx=10, pady=10)

combo_destino = tk.OptionMenu(root, unidad_destino_var, "Celsius", "Fahrenheit", "Kelvin")
combo_destino.grid(row=2, column=1, padx=10, pady=10)

boton_convertir = tk.Button(root, text="Convertir", command=convertir_temperatura)
boton_convertir.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

label_resultado = tk.Label(root, text="Resultado:")
label_resultado.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
