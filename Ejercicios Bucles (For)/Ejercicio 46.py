#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la palabra Abrigo utilizando únicamente una instrucción.
palabra = input("Introduce una palabra: ")

vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"
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