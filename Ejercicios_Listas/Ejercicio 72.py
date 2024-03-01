#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y no deben almacenarse en la lista
import unicodedata

def eliminar_acentos(letra):
    return ''.join(c for c in unicodedata.normalize('NFD', letra) if unicodedata.category(c) != 'Mn')

def ingresar_letras():
    letras_ingresadas = []
    vocales = "aeiouáéíóú"
    while True:
        letra = input("Introduce una letra (o presiona Enter para terminar): ").strip().lower()
        if letra == "":
            break
        elif letra.isalpha() and len(letra) == 1:
            if letra in vocales:
                letra_sin_acento = eliminar_acentos(letra)
                if letra_sin_acento not in letras_ingresadas:
                    letras_ingresadas.append(letra_sin_acento)
                    print(f"La vocal '{letra}' ha sido agregada a la lista.")
                else:
                    print(f"La vocal '{letra}' ya está en la lista.")
            elif letra not in letras_ingresadas:
                letras_ingresadas.append(letra)
                print(f"La letra '{letra}' ha sido agregada a la lista.")
            else:
                print(f"La letra '{letra}' ya está en la lista.")
        else:
            print("Por favor, ingresa solo una letra del alfabeto.")

    return letras_ingresadas

letras = ingresar_letras()
print("Lista de letras ingresadas sin repeticiones:", letras)
