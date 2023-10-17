#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raízcuadrada no de un valor negativo

import math

# Solicitar al usuario que ingrese los coeficientes
a=float(input("Ingrese el coeficiente a: "))
b=float(input("Ingrese el coeficiente b: "))
c=float(input("Ingrese el coeficiente c: "))

# Calcular el discriminante
discriminante = b**2 - 4*a*c
#Comprobar si el discriminante es el negativo
if discriminante < 0:
    print("La raíz no puede ser un valor negativo. ")
else:
    #Calcular las raíces
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b + math.sqrt(discriminante)) / (3*a)
    print(f"El valor x1 es: ",x1)
    print(f"El valor x2 es: ",x2)
input()
