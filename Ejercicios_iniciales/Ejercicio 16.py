#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso (raíz y división).

import math 

número=float(input("Ingrese un número: "))
raiz_cuadrada= float(math.sqrt(número))
resultado_entero= int(round(raiz_cuadrada // 2))

print("La raíz cuadrada de",número,"es: ",raiz_cuadrada)
print("resultado de la división:", resultado_entero)
input()
