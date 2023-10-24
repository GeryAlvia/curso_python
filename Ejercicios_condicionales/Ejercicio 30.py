#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif

frase = input("Introduce una frase: ")
longitud = len(frase)
if longitud == 11:
    print("La longitud de la frase es igual a 11 caracteres.")
elif longitud < 11:
    print("La longitud de la frase es menor de 11 caracteres.")
else:
    print("La longitud de la frase es mayor de 11 caracteres.")
input()