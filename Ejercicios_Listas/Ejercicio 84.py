#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra.
import random
palabras = ["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]
palabra_secreta = random.choice(palabras)
palabra_desordenada = ''.join(random.sample(palabra_secreta, len(palabra_secreta)))
intentos_restantes = 3
while intentos_restantes > 0:
    print("Palabra desordenada:", palabra_desordenada)
    intento = input("Intenta adivinar la palabra: ")
    if intento == palabra_secreta:
        print("¡Correcto! ¡Has adivinado la palabra!")
        break
    else:
        print("Incorrecto. Inténtalo de nuevo.")
        intentos_restantes -= 1
if intentos_restantes == 0:
    print("Lo siento, has agotado tus intentos. La palabra correcta era:", palabra_secreta)
