#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor -99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos
def estadisticas_numeros():
    total_pares = 0
    total_impares = 0
    total_positivos = 0
    total_negativos = 0
    total_ceros = 0
    suma_total = 0
    while True:
        try:
            numero = int(input("Introduce un número: "))
            if numero == -99:
                break
            if numero % 2 == 0:
                total_pares += 1
            else:
                total_impares += 1
            if numero > 0:
                total_positivos += 1
            elif numero < 0:
                total_negativos += 1
            else:
                total_ceros += 1
            suma_total += numero
        except ValueError:
            print("Error: Ingresa un número válido.")
    print("\nEstadísticas:")
    print(f" El número de pares es: {total_pares}")
    print(f" El número de impares es: {total_impares}")
    print(f" El número de positivos es: {total_positivos}")
    print(f" El número de negativos es: {total_negativos}")
    print(f" El total es: {suma_total}")
estadisticas_numeros()
