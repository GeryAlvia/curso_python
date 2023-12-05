#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado o suspendido.
num_notas = int(input("Introduce el número de notas que deseas introducir: "))
for _ in range(num_notas):
    nota = float(input("Introduce la nota: "))
    if nota >= 5:
        print("Asignatura aprobada.")
    else:
        print("Asignatura suspendida.")
