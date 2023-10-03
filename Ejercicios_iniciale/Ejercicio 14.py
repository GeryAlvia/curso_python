#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.

import math
diametro= int(input("Introduce el diámetro del círculo"))
r=diametro/2
pi=math.pi
p=2*pi*r
a=r**2*pi
p=round( p , 1)
a=round( a , 1) 
print("El perímetro del círculo es: ",p)
print("El área del círculo es: ",a)
input()
