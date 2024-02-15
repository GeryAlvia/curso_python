#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números ordenados de menor a mayor.
def main():
    cantidad_numeros = int(input("Introduce un número para saber la cantidad que quieres: "))
    numeros = []
    for i in range(cantidad_numeros):
        numero = int(input("Introduce un número: "))
        numeros.append(numero)
    numeros.sort()
    print(numeros)
if __name__ == "__main__":
    main()
