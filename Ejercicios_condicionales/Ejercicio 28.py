#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.

letra=input("Introduzca una letra: ")
caracter_e=letra.isascii()
mayuscula = letra.isupper()
numero= letra.isdigit()
if numero is True:
    print("El caracter introducido es un numero")


elif mayuscula is True:
    print("La letra es mayuscula")

elif mayuscula is False:
    print("La letra es minuscula")

elif caracter_e is True:
    print("El caracter introducido es un caracter especial")
input()
