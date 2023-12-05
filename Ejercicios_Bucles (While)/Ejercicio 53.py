#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las sumas y el número de repeticiones. Con While
total_sumas = 0 
num_repeticiones = 0 
repetir = 's'
while repetir.lower() == 's':
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero:"))
    suma = num1 + num2
    total_sumas += suma
    num_repeticiones += 1
    print(f"El resultado de la suma es:",suma,"")
    repetir = input("¿Desea repetir la operación? (s/n): ")
print(f"\nLa suma total es:",total_sumas,"y el número de repeticiones es:",num_repeticiones,"")
input()
