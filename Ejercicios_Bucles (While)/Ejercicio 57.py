#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
def adivina_el_numero():
    numero_correcto = random.randint(1, 5)

    while True:
        try:
            guess = int(input("Adivina el número entre 1 y 5: "))
            if 1 <= guess <= 5:
                if guess == numero_correcto:
                    print("Número acertado")
                    break
                else:
                    print("Número no acertado. Inténtalo de nuevo.")
            else:
                print("Por favor, ingresa un número entre 1 y 5.")
        except ValueError:
            print("Error: Ingresa un número válido.")
adivina_el_numero()
