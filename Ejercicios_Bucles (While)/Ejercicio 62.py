#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
def numeros_pares_impares():
    try:
        numero1 = int(input("Ingresa el primer número: "))
        numero2 = int(input("Ingresa el segundo número: "))
        if numero1 > numero2:
            numero1, numero2 = numero2, numero1
        print(f"{numero1}\n{numero2}")
        pares = []
        impares = []
        for numero in range(numero1, numero2 + 1):
            if numero % 2 == 0:
                pares.append(str(numero))
            else:
                impares.append(str(numero))
        print(f"Los números pares son: {'-'.join(pares)}")
        print(f"Los números impares son: {'-'.join(impares)}")
    except ValueError:
        print("Error: Ingresa números válidos.")
numeros_pares_impares()
