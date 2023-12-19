#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
def adivina_el_numero(intentos):
    numero_correcto = random.randint(1, 5)

    while intentos > 0:
        try:
            guess = int(input("Adivina el número entre 1 y 5: "))
            if 1 <= guess <= 5:
                if guess == numero_correcto:
                    print("¡Correcto! ¡Has adivinado el número!")
                    return
                else:
                    print(f"Incorrecto. Te quedan {intentos - 1} intentos.")
            else:
                print("Por favor, ingresa un número entre 1 y 5.")
        except ValueError:
            print("Error: Ingresa un número válido.")

        intentos -= 1

    print(f"Lo siento, te has quedado sin intentos. El número correcto era {numero_correcto}.")
adivina_el_numero(intentos=3)
