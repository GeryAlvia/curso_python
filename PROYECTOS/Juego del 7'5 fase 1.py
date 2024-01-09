#Fase 1 del 7'5
import random

def obtener_carta():
    return random.choice([i for i in range(1, 13) if i not in [8, 9]])

def valor_carta(carta):
    if carta <= 7:
        return carta
    elif carta <= 12:
        return 0.5
    else:
        return None

def jugar_partida():
    puntuacion = 0
    
    while True:
        carta = obtener_carta()
        print(f"Carta actual: {carta}")
        
        valor = valor_carta(carta)
        if valor is not None:
            puntuacion += valor
            print(f"Tu puntuación actual es: {puntuacion}")
            
            if puntuacion == 7.5:
                print("Enhorabuena, has ganado la partida!")
                break
            elif puntuacion > 7.5:
                print("Has perdido la partida!")
                break
            elif puntuacion >= 6 and puntuacion <= 7:
                print("Has sido un poco conservador.")
                break
        else:
            print("Error: Carta inválida.")
            break

        decision = input("¿Quieres tomar otra carta? (s/n): ").lower()
        
        if decision == 'n':
            if puntuacion < 6:
                print("Quizás deberías arriesgar un poco, ¿no?")
            else:
                print("Te has plantado. ¡Buena decisión!")
            break
        elif decision != 's':
            print("Por favor, introduce 's' para tomar otra carta o 'n' para plantarte.")
while True:
    jugar_partida()
    otra_partida = input("¿Quieres jugar otra partida? (s/n): ").lower()
    
    if otra_partida != 's':
        print("Gracias por jugar. ¡Hasta luego!")
        break
