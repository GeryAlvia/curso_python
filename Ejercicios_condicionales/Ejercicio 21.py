#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raízcuadrada no de un valor negativo
import math
a=float(input("Ingrese el coeficiente a: "))
b=float(input("Ingrese el coeficiente b: "))
c=float(input("Ingrese el coeficiente c: "))
discriminante = b**2 - 4*a*c
if discriminante < 0:
    print("La raíz no puede ser un valor negativo. ")
else:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b + math.sqrt(discriminante)) / (3*a)
    print(f"El valor x1 es: ",x1)
    print(f"El valor x2 es: ",x2)
input()
