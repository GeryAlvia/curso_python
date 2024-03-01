#76-77. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.
lista1 = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', '2', 'i']
letras = [char for char in lista1 if char.isalpha()]
numeros = [int(char) for char in lista1 if char.isdigit()]
orden = input("¿En qué orden quieres visualizar las letras? (ascendente/descendente): ").lower()
if orden == "ascendente":
    letras.sort(key=str.lower)
elif orden == "descendente":
    letras.sort(key=str.lower, reverse=True)
else:
    print("Opción de orden incorrecta. Se mostrarán en orden original.")
numeros.sort()
print("Letras ordenadas:")
for letra in letras:
    print(letra)
print("\nNúmeros ordenados:")
for numero in numeros:
    print(numero)
