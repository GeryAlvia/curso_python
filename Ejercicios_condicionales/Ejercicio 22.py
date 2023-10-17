#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.

nota=float(input("Introuzca una nota entre 0 y 10: "))
if nota>0 and nota<10:
    if nota <5:
        print(f"Has sacado un {nota} y has suspendido")
    if nota>=5:
        print(f"Has sacado un {nota} y has aprobado")

else:
    print("El numero no está entre los valores")
input()
