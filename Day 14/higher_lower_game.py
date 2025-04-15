import random
import os
from datos_famosos import famosos

# Función para limpiar la consola
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar cabecera del juego
def mostrar_bienvenida():
    print("🌟 Bienvenido al juego *Higher Lower* de Famosos 🌟")
    print("🎯 Tu objetivo es adivinar quién tiene más seguidores en Instagram.")
    print("🔁 Si aciertas, ¡continúas sumando puntos!")
    print("😵 Si fallas, el juego termina.")
    print("¿Estás listo para jugar? (sí/no)")

# Lista de nombres para elegir aleatoriamente
nombres_famosos = list(famosos.keys())
score = 0

# Inicio del juego
limpiar_pantalla()
mostrar_bienvenida()
play = input("👉 ").lower()

while play == "sí" or play == "si":
    limpiar_pantalla()
    nombre1, nombre2 = random.sample(nombres_famosos, 2)
    famoso1 = famosos[nombre1]
    famoso2 = famosos[nombre2]

    while True:
        limpiar_pantalla()
        print(f"🔥 Ronda actual | Puntuación: {score}")
        print("═════════════════════════════════════════════════════")
        print(f"👤 Famoso 1: {nombre1}")
        print(f"   Categoría: {famoso1['categoria'].capitalize()}")
        print(f"   Nacionalidad: {famoso1['nacionalidad'].capitalize()}")
        print(" VS ")
        print(f"👤 Famoso 2: {nombre2}")
        print(f"   Categoría: {famoso2['categoria'].capitalize()}")
        print(f"   Nacionalidad: {famoso2['nacionalidad'].capitalize()}")
        print("═════════════════════════════════════════════════════")
        guess = input("🤔 ¿Quién tiene más seguidores en Instagram? (1 o 2): ")

        ganador = "1" if famoso1["seguidores"] > famoso2["seguidores"] else "2"

        if guess == ganador:
            score += 1
            print("\n✅ ¡Correcto! 🎉")
        else:
            print("\n❌ ¡Incorrecto! 😢")
            print("════════ RESULTADOS ════════")
            print(f"{nombre1}: {famoso1['seguidores']:,} seguidores")
            print(f"{nombre2}: {famoso2['seguidores']:,} seguidores")
            print(f"🏁 Puntuación final: {score}")
            print("¿Quieres jugar de nuevo? (sí/no)")
            score = 0
            play = input("👉 ").lower()
            break

        print("════════ RESULTADOS ════════")
        print(f"{nombre1}: {famoso1['seguidores']:,} seguidores")
        print(f"{nombre2}: {famoso2['seguidores']:,} seguidores")
        print(f"⭐ Puntuación actual: {score}")
        input("\nPresiona Enter para continuar a la siguiente ronda...")

        # El famoso con más seguidores se queda, el otro cambia
        if ganador == "2":
            nombre1 = nombre2
            famoso1 = famoso2

        nombre2 = random.choice([n for n in nombres_famosos if n != nombre1])
        famoso2 = famosos[nombre2]
