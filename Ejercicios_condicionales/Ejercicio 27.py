#Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla

var1=input("Introduce una letra:  ")

numero=var1.isdigit()
if numero is True:
    print("El valor introducido es un numero.")
elif numero is False:
    if 'A' <= var1 <= 'Z':
            mayuscula = True
    else:
            mayuscula = False
    if mayuscula:
            print("La letra ingresada está en mayúscula.")
    else:
            print("La letra ingresada está en minúscula.")