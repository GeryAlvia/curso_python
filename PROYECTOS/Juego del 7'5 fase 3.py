#Fase 3 del 7'5
import random
import time
def dar_carta():
    carta = random.randint(1, 12)
    if carta in [8, 9]:
        return dar_carta()
    elif carta in [10, 11, 12]:
        return 0.5
    else:
        return carta
def gestionar_partida():
    total_jugador = 0
    total_banca = 0
    cartas_jugador = []
    cartas_banca = []
    alias = input("Introduce tu alias para comenzar el juego: ")
    print(f"Bienvenido, {alias}, antes de comenzar a jugar tienes que saber que los numeros 10, 11 y 12 pasan a ser directamente 0,5.")
    while total_jugador < 7.5:
        respuesta = input(f"{alias}, ¿quieres otra carta? (s/n): ")
        if respuesta.lower() == 's':
            nueva_carta_jugador = dar_carta()
            cartas_jugador.append(nueva_carta_jugador)
            total_jugador += nueva_carta_jugador
            print(f"Nueva carta de {alias}: {nueva_carta_jugador} Total de {alias}: {total_jugador}")
            time.sleep(1) 
        elif respuesta.lower() == 'n':
            print(f"{alias} se ha plantado.")
            break
        else:
            print("Para seguir jugando debes de introducir's/n'.")
    print("Turno de la banca:")
    while total_banca < 5.0:
        nueva_carta_banca = dar_carta()
        cartas_banca.append(nueva_carta_banca)
        total_banca += nueva_carta_banca
        print(f"Nueva carta de la banca: {nueva_carta_banca} Total de la banca: {total_banca}")
        time.sleep(1.5) 
    print(f"Cartas de {alias}: {cartas_jugador} Total de {alias}: {total_jugador}")
    print(f"Cartas de la banca: {cartas_banca} Total de la banca: {total_banca}")

    if total_jugador > 7.5:
        print("¡La banca gana! El jugador se ha pasado de 7.5.")
    elif total_banca > 7.5:
        print(f"¡Felicidades {alias}! La banca se ha pasado de 7.5.")
    elif total_jugador == total_banca:
        print("¡Empate! El jugador y la banca tienen la misma puntuación.")
    elif total_jugador > total_banca:
        print(f"¡Has ganado {alias}! Has obtenido una puntuación mayor que la banca.")
    else:
        print("¡La banca gana! Ha obtenido una puntuación mayor que el jugador.")
while True:
    gestionar_partida()
    jugar_nueva_partida = input("¿Quieres jugar otra partida? (s/n): ")
    if jugar_nueva_partida.lower() != 's':
        print("¡Gracias por jugar! QUE VALLA BIEN 🙂.")
        break

