#66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo se comporta el dado en lanzamientos producidos durante aprox 3 segundos.
import random
import time
def lanzamiento_dado():
    inicio_tiempo = time.time()
    resultados = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    while time.time() - inicio_tiempo < 3:
        resultado = random.randint(1, 6)
        resultados[resultado] += 1
        time.sleep(0.1)
    print("Resultados del lanzamiento del dado durante aprox. 3 segundos:")
    for numero, frecuencia in resultados.items():
        print(f"Número {numero}: {frecuencia} veces")
lanzamiento_dado()
