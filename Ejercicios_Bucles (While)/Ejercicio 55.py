#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
total_sumas = 0
num_repeticiones = 0
while total_sumas <= 50 or total_sumas % 2 == 0:
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))
    suma = num1 + num2
    total_sumas += suma
    num_repeticiones += 1
    mensaje_acumulado = "suma" if num_repeticiones == 1 else "sumas"

    print(f"El resultado de la suma es: {suma}")
    print(f"Acumulado después de {num_repeticiones} {mensaje_acumulado}: {total_sumas}")
print(f"\nLa suma total es: {total_sumas} después de {num_repeticiones} {mensaje_acumulado}")
input()
