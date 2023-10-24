#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.

frase = "A quién madruga Dios ayuda."
palabras_a_verificar = ["madruga", "Dios", "dios"]

for palabra in palabras_a_verificar:
    if palabra in frase:
        indice = frase.index(palabra)
        print(f"La palabra '{palabra}' está en la posición de índice {indice}.")
    else:
        print(f"La palabra '{palabra}' no está en la frase.")
