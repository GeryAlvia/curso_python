#65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor.
def encontrar_mayor_menor():
    mayor = float('-inf') 
    menor = float('inf')  
    while True:
        try:
            numero = float(input("Introduce un número (-99 para salir): "))
            if numero == -99:
                break
            if numero > mayor:
                mayor = numero
            if numero < menor:
                menor = numero
        except ValueError:
            print("Error: Ingresa un número válido.")
    if mayor == float('-inf') and menor == float('inf'):
        print("No se introdujeron números.")
    else:
        print(f"\nEl número mayor es: {mayor}")
        print(f"El número menor es: {menor}")
encontrar_mayor_menor()
