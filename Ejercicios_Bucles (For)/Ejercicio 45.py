#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string distinguiendo vocales y las consonantes:
palabra = input("Introduce una palabra: ")
vocales = "aeiouáéíóú"
consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
vocales_encontradas = ""
consonantes_encontradas = ""
for letra in palabra:
    if letra in vocales:
        vocales_encontradas += letra
    elif letra in consonantes:
        consonantes_encontradas += letra
print(f"Las vocales de la palabra",palabra,"son: ",vocales_encontradas,"")
print(f"Las consonantes de la palabra",palabra,"son: ",consonantes_encontradas,"")
input()