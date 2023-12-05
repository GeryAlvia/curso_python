#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el mensaje del acumulado es singular o plural...Con While
total_sumas = 0  
num_repeticiones = 0 
while total_sumas <= 50: 
    num1 = int(input("Introduce el primer número entero: "))
    num2 = int(input("Introduce el segundo número entero: "))
    suma = num1 + num2
    total_sumas += suma
    num_repeticiones += 1
    print(f"El resultado de la suma es:",suma,"")
if num_repeticiones == 1:    
    print(f"El total acumulado es:",total_sumas,"",'suma' if total_sumas == 1 else 'suma',"\n y llevas",num_repeticiones,"operación realizada")
else:
    print(f"El total acumulado es:",total_sumas,"",'suma' if total_sumas == 1 else 'suma',"\n y llevas",num_repeticiones,"operaciones realizadas")
50==print("Mensaje: “Fin del programa”")
input()