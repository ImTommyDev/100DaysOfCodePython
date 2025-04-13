import random

def calcular_puntuacion(mano):
    return sum(mano)  # No se ajusta el As a 1

def blackjack():
    baraja = [11,2,3,4,5,6,7,8,9,10,10,10,10] * 4
    random.shuffle(baraja)

    mano_jugador = [baraja.pop(), baraja.pop()]
    mano_dealer = [baraja.pop(), baraja.pop()]
    
    puntuacion_jugador = calcular_puntuacion(mano_jugador)
    puntuacion_dealer = calcular_puntuacion(mano_dealer)

    print(f'Cartas del jugador: {mano_jugador}, Total: {puntuacion_jugador}')
    print(f'Cartas del dealer: [{mano_dealer[0]}, _]')

    while puntuacion_jugador < 21:
        respuesta = input('¿Quieres pedir otra carta? (s/n): ').lower()
        if respuesta != 's':
            break
        mano_jugador.append(baraja.pop())
        puntuacion_jugador = calcular_puntuacion(mano_jugador)
        print(f'Cartas del jugador: {mano_jugador}, Total: {puntuacion_jugador}')
        
        if puntuacion_jugador > 21:
            print('Te has pasado de 21. ¡Perdiste!')
            break

    if puntuacion_jugador <= 21:
        print(f'\nCartas del dealer: {mano_dealer}, Total: {puntuacion_dealer}')
        while puntuacion_dealer < 17:
            mano_dealer.append(baraja.pop())
            puntuacion_dealer = calcular_puntuacion(mano_dealer)
            print(f'Cartas del dealer: {mano_dealer}, Total: {puntuacion_dealer}')
        
        if puntuacion_dealer > 21:
            print('El dealer se ha pasado de 21. ¡Ganaste!')
        elif puntuacion_jugador > puntuacion_dealer:
            print('¡Ganaste!')
        elif puntuacion_jugador < puntuacion_dealer:
            print('Perdiste.')
        else:
            print('Empate.')

    print('\n¿Quieres jugar de nuevo? (s/n)')
    if input().lower() == 's':
        blackjack()
    else:
        print('¡Hasta pronto!')

print("""
🎲 ¡Bienvenido a Blackjack! 🃏

Las reglas son simples:

🔹 El objetivo es llegar a 21 puntos sin pasarse.
🔹 El valor de las cartas es el siguiente:
   - As: 11 puntos (no cambia a 1)
   - Cartas del 2 al 10: su valor nominal
   - J, Q, K: 10 puntos

📋 Reglas del juego:
- Si el jugador y el dealer tienen la misma puntuación, es un empate.
- Si el jugador supera los 21 puntos, pierde automáticamente.
- Si el dealer supera los 21 puntos, el jugador gana automáticamente.
- El dealer debe pedir cartas hasta alcanzar al menos 17 puntos.
- Si el jugador tiene una puntuación mayor que el dealer, gana. En caso contrario, pierde.

¿Quieres jugar? (s/n)
""")

if input().lower() == 's':
    blackjack()
else:
    print('¡Hasta pronto!')
