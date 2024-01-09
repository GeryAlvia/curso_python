#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. Utiliza únicamente el while
def tabla_de_multiplicar():
    try:
        numero = int(input("Ingresa un número para obtener su tabla de multiplicar: "))
        contador = 1
        while contador <= 10:
            resultado = numero * contador
            print(resultado)
            contador += 1
    except ValueError:
        print("Error: Ingresa un número válido.")
tabla_de_multiplicar()
input()