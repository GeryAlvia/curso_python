#Fase 2 del 7'5
import random
print("                   ♠️♥️ HOLA BIENVENIDO AL JUEGO DEL 7,5 ♦️♣️                       ")
print("Ademas tienes que saber que los numeros 10, 11 y 12 pasan a ser directamente 0,5")
def dar_carta():
    carta = random.randint(1, 12)
    if carta in [8, 9]:
        return dar_carta()
    elif carta in [10, 11, 12]:
        return 0.5
    else:
        return carta

def gestionar_partida(puntos):
    total = 0
    cartas = []
    primera_carta = dar_carta()
    cartas.append(primera_carta)
    total += primera_carta
    print(f"Primera carta: {primera_carta} Total: {total}")

    while total < 7.5:
        respuesta = input("¿Quieres escoger otra carta? (s/n): ")
        if respuesta.lower() == 's':
            nueva_carta = dar_carta()
            cartas.append(nueva_carta)
            total += nueva_carta
            print(f"Nueva carta: {nueva_carta} Total: {total}")
        elif respuesta.lower() == 'n':
            print("Te has plantado.")
            break
        else:
            print("Respuesta no válida. Escribe 's/n' para seguir jugando.")

    print(f"Cartas: {cartas} Total final: {total}")

    if total == 7.5:
        puntos += 10
        print("¡Enhorabuena, has ganado la partida y obtienes 10 puntos!")
    elif total > 7.5:
        puntos -= 10
        print("Has perdido la partida. Pierdes 10 puntos.")
    elif 6 <= total <= 7:
        puntos += 5
        print("Has sido un poco conservador. Ganaste 5 puntos.")
    elif total < 6:
        puntos -= 5
        print("Quizás deberías arriesgar un poco, ¿no? Pierdes 5 puntos.")

    return puntos

puntos = 100

while puntos > 0:
    print(f"Tus puntos actuales: {puntos}")
    jugar_nueva_partida = input("Jugar partida? (s/n): ")

    if jugar_nueva_partida.lower() != 's':
        print("Acuerdate de que aún te quedan puntos para continuar jugando 🙂.")
        exit()

    puntos = gestionar_partida(puntos)
print("😢Te has quedado sin puntos. Haber si la próxima vez lo haces mejor ¡Que vaya bien!")
