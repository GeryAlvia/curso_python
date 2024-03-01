#81. A partir de una lista definida, busca el método apropiado para que se visualice un valor de la lista al azar.
import random
palabras = ['casa', 'barco', 'gato', 'perro', 'madera', 'agua', 'puente', 'pantalón']
palabra_al_azar = random.choice(palabras)
print("Palabra seleccionada al azar:", palabra_al_azar)

