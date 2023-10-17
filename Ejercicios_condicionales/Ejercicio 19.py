#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales

numero_1=int(input("Introduzca un numero: "))
numero_2=int(input("Introduzca un numero: "))
if numero_1<numero_2:
    print(f"El numero {numero_1} es menor que el numero {numero_2}")

if numero_1>numero_2:
    print(f"El numero {numero_1} es mayor que el numero {numero_2}")

if numero_1==numero_2:
    print("Ambos numeros son iguales")
input()
          
