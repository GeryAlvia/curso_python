#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista = ['a', 'b', 'D', 'x', 'r', 'X', '3', 'h', 'w', 'i']
while True:
    valor = input("Introduce el valor que deseas eliminar: ")
    if valor.isdigit():
        if valor in lista:
            lista.remove(valor)
            print("Valor eliminado:", valor)
            print("Lista resultante:", lista)
        else:
            print("El valor introducido no está en la lista.")
    else:
        print("Introduce valor numérico.")

    continuar = input("Deseas introducir otro valor? (s/n): ")
    if continuar.lower() != 's':
        break

print("Lista final:", lista)
