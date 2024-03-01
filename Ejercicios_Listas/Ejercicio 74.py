#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de entre las 2 listas.
def comprobar_repetidos(lista1, lista2):
    repetidos = []
    no_repetidos = []

    for palabra in lista1:
        if palabra in lista2:
            repetidos.append(palabra)
        else:
            no_repetidos.append(palabra)

    return repetidos, no_repetidos

lista1 = ["casa", "mesa", "sal", "sol", "agua", "tres", "tren", "luz"]
lista2 = ["casa", "sol", "pan"]

repetidos, no_repetidos = comprobar_repetidos(lista1, lista2)

print("Palabras repetidas:", repetidos)
print("Palabras no repetidas:", no_repetidos)

