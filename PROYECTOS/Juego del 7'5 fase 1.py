#Fase 1 del 7'5
import random
def dar_carta():
    carta = random.randint(1, 12)
    if carta in [8, 9]:
        return dar_carta()
    elif carta in [10, 11, 12]:
        return 0.5
    else:
        return carta
def gestionar_partida():
    total = 0
    cartas = []
    primera_carta = dar_carta()
    cartas.append(primera_carta)
    total += primera_carta
    print(f"Primera carta: {primera_carta} Total: {total}")
    while total < 7.5:
        respuesta = input("Quieres otra carta? (s/n): ")
        if respuesta.lower() == 's':
            nueva_carta = dar_carta()
            cartas.append(nueva_carta)
            total += nueva_carta
            print(f"Nueva carta: {nueva_carta} Total: {total}")
        elif respuesta.lower() == 'n':
            print("Te has plantado.")
            break
        else:
            print("Respuesta no válida. Ingresa 's/n'.")
    print(f"Cartas: {cartas} Total final: {total}")
    if total == 7.5:
        print("¡Enhorabuena, has ganado la partida!")
    elif total > 7.5:
        print("Has perdido la partida.")
    elif 6 <= total <= 7:
        print("Has sido un poco conservador.")
    elif total < 6:
        print("Quizás deberías arriesgar un poco, ¿no?")
while True:
    gestionar_partida()
    jugar_nueva_partida = input("Quieres jugar otra partida? (s/n): ")
    if jugar_nueva_partida.lower() != 's':
        print("¡Gracias por jugar! Hasta luego.")
        break
input()
