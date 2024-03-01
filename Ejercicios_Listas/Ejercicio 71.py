#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.
letras = []
while True:
    entrada = input("Introduce una letra: ")
    if entrada.isalpha():  # Verifica si la entrada es una letra
        letra = entrada.lower()  # Convertimos la letra a minúscula  
        if letra not in letras:
            letras.append(letra)
        else:
            print("¡La letra ya está en la lista!")
    else:
        print("Entrada inválida. Debes introducir una letra.")
    repetir = input("¿Deseas repetir? (s/n): ")
    if repetir.lower() != 's':
        break
print(letras)
