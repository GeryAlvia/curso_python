#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b la secuencia en descenso. Respeta el formato de salida
var1= int(input("Introduce el primer intervalo: "))
var2= int(input("Introduce el segundo intervalo: "))
print("Rango de números:")
if var1<var2:
    for n in range(var1,var2 + 1):
        print(n, end="-")
else:
    for n in range(var1,var2-1,-1):
        print(n, end="-")
input()

