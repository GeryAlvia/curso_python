#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir notas inferiores a 0 y superiores a 10
num_notas = int(input("Introduce el número de notas que deseas introducir: "))

for _ in range(num_notas):
    while True:
        try:
            nota = float(input("Introduce la nota: "))
            if 0 <= nota <= 10:
                break  
            else:
                print("Error:   Has introducido la nota equivocada")
        except ValueError:
            print("Error: Ingresa un número válido.")

    if nota >= 5:
        print("Asignatura aprobada.")
    else:
        print("Asignatura suspendida.")
