#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en esta lista no deben almacenarse las letras que se han introducido repetidas.
def main():
    palabras = input("Introduce las palabras separadas por espacio: ").split()
    lista1 = palabras[:]
    lista2 = palabras[:]
    lista1.sort()
    lista2.sort(reverse=True)
    print("Contenidos de lista1 en orden ascendente: ")
    for palabra in lista1:
        print(palabra, end=" ")
    print("Contenidos de lista2 en orden descendente: ")
    for palabra in lista2:
        print(palabra, end=" ")
if __name__ == "__main__":
    main()
