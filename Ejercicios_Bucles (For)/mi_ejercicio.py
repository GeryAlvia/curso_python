import random
import tkinter as tk
from tkinter import messagebox

class JuegoAdivinaNumero:
    def __init__(self, master):
        self.master = master
        self.master.title("Adivina el Número")

        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

        self.label = tk.Label(master, text="Adivina el número (entre 1 y 100):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Adivinar", command=self.verificar_numero)
        self.button.pack()

    def verificar_numero(self):
        try:
            intento = int(self.entry.get())
            self.intentos += 1

            if intento < self.numero_secreto:
                messagebox.showinfo("Adivina el Número", "El número es mayor. Intenta de nuevo.")
            elif intento > self.numero_secreto:
                messagebox.showinfo("Adivina el Número", "El número es menor. Intenta de nuevo.")
            else:
                messagebox.showinfo("Adivina el Número", f"¡Felicidades! Has adivinado el número en {self.intentos} intentos.")
                self.master.destroy()
        except ValueError:
            messagebox.showerror("Error", "Ingresa un número válido.")

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoAdivinaNumero(root)
    root.mainloop()
