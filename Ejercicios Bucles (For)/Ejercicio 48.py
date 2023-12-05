#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario tenga x oportunidades para ver si letra introducida está en esa palabra.
palabra_secreta = input("Introduce la palabra secreta: ")
longitud_palabra = len(palabra_secreta)
intentos_maximos = longitud_palabra
for intento in range(1, intentos_maximos + 1):
    letra = input(f"Introduce una letra: ")
    if letra in palabra_secreta:
        print(f"La letra '",letra,"' existe.")
    else:
        print(f"La letra '",letra,"' no existe.")
print("La palabra secreta era:", palabra_secreta)
input()



