#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número de veces que se repite cada número.
import random
def lanzamiento_dado():
    resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for _ in range(100):
        resultado = random.randint(1, 6)
        resultados[resultado] += 1
    print("Resultados del lanzamiento del dado (100 veces):")
    for numero, frecuencia in resultados.items():
        print(f"Número {numero}: {frecuencia} veces")
lanzamiento_dado()
