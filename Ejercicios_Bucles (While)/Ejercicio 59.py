#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe mostrarse por pantalla un mensaje y el número de intentos.
import random
def adivina_numero():
    numero_correcto = random.randint(0, 1000)
    intentos = 0

    while True:
        try:
            guess = int(input("Intenta adivinar el número entre 0 y 1000: "))
            intentos += 1
            if guess == numero_correcto:
                print(f"¡Correcto! Has adivinado el número {numero_correcto} en {intentos} intentos.")
                return
            elif guess < numero_correcto:
                print("Incorrecto. El número es mayor. Inténtalo de nuevo.")
            else:
                print("Incorrecto. El número es menor. Inténtalo de nuevo.")
        except ValueError:
            print("Error: Ingresa un número válido.")
adivina_numero()
