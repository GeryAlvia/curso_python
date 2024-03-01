#85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el programa debe mostrar la media y mediana los todos los alumnos introducidos
import statistics
def ingresar_calificaciones():
    calificaciones_ingles = []
    calificaciones_castellano = []
    calificaciones_catalan = []
    while True:
        nombre = input("Introduce estudiante: ")
        nota_ingles = float(input("Nota inglés: "))
        nota_castellano = float(input("Nota castellano: "))
        nota_catalan = float(input("Nota catalán: "))
        calificaciones_ingles.append(nota_ingles)
        calificaciones_castellano.append(nota_castellano)
        calificaciones_catalan.append(nota_catalan)

        otro_alumno = input("Deseas introducir otro alumno (s/n): ")
        if otro_alumno.lower() != 's':
            break

    return calificaciones_ingles, calificaciones_castellano, calificaciones_catalan

def calcular_media_mediana(calificaciones):
    media_ingles = statistics.mean(calificaciones[0])
    mediana_ingles = statistics.median(calificaciones[0])

    media_castellano = statistics.mean(calificaciones[1])
    mediana_castellano = statistics.median(calificaciones[1])

    media_catalan = statistics.mean(calificaciones[2])
    mediana_catalan = statistics.median(calificaciones[2])

    return media_ingles, mediana_ingles, media_castellano, mediana_castellano, media_catalan, mediana_catalan

def main():
    print("Bienvenido al programa de gestión de calificaciones")
    calificaciones = ingresar_calificaciones()

    media_ingles, mediana_ingles, media_castellano, mediana_castellano, media_catalan, mediana_catalan = calcular_media_mediana(calificaciones)
    print("\nLa media en inglés es:", media_ingles)
    print("La media en castellano es:", media_castellano)
    print("La media en catalán es:", media_catalan)
    print("La mediana en inglés es:", mediana_ingles)
    print("La mediana en castellano es:", mediana_castellano)
    print("La mediana en catalán es:", mediana_catalan)
    print("\nCalificaciones en inglés:", calificaciones[0])
    print("Calificaciones en castellano:", calificaciones[1])
    print("Calificaciones en catalán:", calificaciones[2])
    print("\nRESUMEN")
    print("La media en inglés es:", media_ingles)
    print("La media en castellano es:", media_castellano)
    print("La media en catalán es:", media_catalan)
    print("La mediana en inglés es:", mediana_ingles)
    print("La mediana en castellano es:", mediana_castellano)
    print("La mediana en catalán es:", mediana_catalan)

if __name__ == "__main__":
    main()
