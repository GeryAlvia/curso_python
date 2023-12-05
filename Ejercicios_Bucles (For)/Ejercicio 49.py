#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te indique en qué posición de la palabra se encuentra la letra.
palabra_secreta = input("Introduce la palabra secreta: ").lower()
while True:
    letra = input("Introduce una letra o escribe 'salir' para terminar: ").lower()
    if letra == 'salir':
        break
    if letra.isalpha() and len(letra) == 1:
        if letra in palabra_secreta:
            posiciones = [i for i, char in enumerate(palabra_secreta) if char == letra]
            print(f"¡Correcto! La letra '{letra}' está en la posición {', '.join(map(str, posiciones))} de la palabra.")
        else:
            print(f"Incorrecto. La letra '{letra}' no está en la palabra.")
    else:
        print("Por favor, ingresa una letra válida.")
print("Terminaste el juego. La palabra secreta era:", palabra_secreta)
input()