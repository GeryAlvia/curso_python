#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas

frase = "A quién madruga Dios ayuda."
frase_minusculas = frase.lower()
palabras_a_verificar = ["Dios", "dios", "madruga"]
palabras_a_verificar = [palabra.lower() for palabra in palabras_a_verificar]
for palabra in palabras_a_verificar:
    if palabra in frase_minusculas:
        indice = frase_minusculas.index(palabra)
        print(f"La palabra '{palabra}' está en la posición de índice {indice}.")
    else:
        print(f"La palabra '{palabra}' no está en la frase.")