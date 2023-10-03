#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.

import math

pi=math.pi
r=int(input("Introduce el valor del radio"))
h=int(input("Introduce la altura del cilindro"))
diam=r*2
ab=r**2*pi
ar=diam*pi*h
at=ab*2+ar
V=ab*h
V=round( V , 2)
at=round( at, 2)
print("El área de un cilindro es: ", at)
print("El volumen de un cilindro es: ", V)
input()

