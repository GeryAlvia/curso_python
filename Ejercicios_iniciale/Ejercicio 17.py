#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso(en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.

p=float(input("Introduce tu peso en Kg: "))
a=float(input("Introduce tu altura en m: "))
imc=p/(a**2)
imcr=round(imc,2)
if imc>= 25:
    print("Si pesas", p, "y mides", float(a),"Tienes un IMC de",imcr, "Hay sobrepeso.")
else:
    print("Si pesas", p, "y mides", float(a),"Tienes un IMC de",imcr)