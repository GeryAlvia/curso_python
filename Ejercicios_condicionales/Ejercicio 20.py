#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10

numero_1=int(input("Introduzca un numero de entre 0 y 10: "))
numero_2=int(input("Introduzca un numero de entre 0 y 10: "))


if (numero_1>0 and numero_1<10) and (numero_2>0 and numero_2<10):

    numero_1<numero_2
    print(f"El numero {numero_1} es menor que el numero {numero_2}")

    numero_1>numero_2
    print(f"El numero {numero_2} es mayor que el numero {numero_1}")


else:
    print("Uno de los numeros esta fuera de los rangos")
input()
