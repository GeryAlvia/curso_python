#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine la palabra
import random
palabras = ["casa", "barco", "gato", "perro", "madera", "agua", "puente","pantalón"]
palabra_secreta = random.choice(palabras)
adivinanza = ""
while adivinanza != palabra_secreta:
    adivinanza = input("Introduce la palabra secreta: ")
    if adivinanza == palabra_secreta:
        print("ACERTASTE")
    else:
        print("SIGUE JUGANDO")

