#61. A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es superior o igual a 40.
def tabla_de_multiplicar():
    try:
        numero = int(input("Ingresa un número para obtener su tabla de multiplicar: "))
        contador = 1
        while contador <= 10:
            resultado = numero * contador
            print(resultado)
            contador += 1
            if resultado >= 40:
                print("Fin del programa.")
                break
    except ValueError:
        print("Error: Ingresa un número válido.")
tabla_de_multiplicar()
input()
