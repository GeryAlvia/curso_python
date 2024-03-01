#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el formato de entrada y salida tal y como se muestra en el testeo.
def main():
    cantidad_palabras = int(input("Introduce la cantidad de palabras: "))
    lista1 = []
    for i in range(1, cantidad_palabras + 1):
        palabra = input(f"Introduce {i} palabra: ")
        lista1.append(palabra)
    lista2 = lista1[:]
    lista1.sort()
    lista2.sort(reverse=True)
    print("lista1 contiene:", lista1)
    print("lista2 contiene:", lista2)
if __name__ == "__main__":
    main()