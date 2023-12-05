#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por pantalla. El programa preguntará si deseas o no repetir la operación. Con While
repetir = 's' 
while repetir.lower() == 's': 
    var1 = int(input("Introduce el primer número entero: "))
    var2 = int(input("Introduce el segundo número entero: "))
    suma = var1 + var2
    print(f"El resultado de la suma es: ",suma,"")
    repetir = input("¿Desea repetir la operación? (s/n): ")
n=print("Mensaje: “Programa finalizado”")
input()
