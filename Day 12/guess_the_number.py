import random

# Adivinador de números

# Le preguntamos al usuario si quiere jugar
print("🎮 ¿Quieres jugar? (s/n)")
play = input().lower()

# Mientras el usuario quiera jugar, seguimos
while play == "s":
    # Generamos un nuevo número aleatorio entre 1 y 100
    number = random.randint(1, 100)

    print("\n🤔 ¿Modo fácil o difícil? (f/d)")
    mode = input().lower()

    if mode == "f":
        attempts = 10
    elif mode == "d":
        attempts = 5
    else:
        print("⚠️ Modo no válido. Intenta de nuevo.\n")
        continue

    print(f"\n🔢 Tienes {attempts} intentos para adivinar el número entre 1 y 100.")
    
    while attempts > 0:
        print("\n🔎 Introduce un número:")
        try:
            guess = int(input())
        except ValueError:
            print("⚠️ Por favor, introduce un número válido.")
            continue

        if guess == number:
            print("\n🎉 ¡Has adivinado el número! 🎉")
            break
        elif guess < number:
            print("⬆️ El número es mayor")
        else:
            print("⬇️ El número es menor")
        
        attempts -= 1

        if attempts > 0:
            print(f"🕒 Te quedan {attempts} intento(s)")
        else:
            print(f"\n💥 ¡Has perdido! El número era {number}")
    
    print("\n==============================")
    print("🔁 ¿Quieres jugar de nuevo? (s/n)")
    play = input().lower()
    print("==============================\n")
