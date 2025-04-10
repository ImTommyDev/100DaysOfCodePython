import random

# Título en ASCII
print(r'''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')

print("---- Bienvenido a Hangman ----")
print('''\nLas reglas son simples:
1. Adivina la palabra secreta letra por letra.
2. Si eliges una letra correcta, se mostrará en su lugar.
3. Si eliges una letra incorrecta, perderás una vida.
4. Tienes 6 vidas en total.
5. Si adivinas la palabra antes de perder todas las vidas, ganas.\n''')

# Dibujo del ahorcado por nivel de error
ahorcado = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========''', 
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========='''
]

respuesta = input("¿Quieres jugar? (si/no): ").lower()
if respuesta != "si":
    print("¡Hasta luego!")
else:
    # Lista de palabras
    palabras = ["python", "programacion", "desarrollo", "computadora", "algoritmo", 
                "tecnologia", "software", "hardware", "internet", "redes", "datos"]

    palabra_secreta = list(random.choice(palabras))
    palabra_usuario = ["_"] * len(palabra_secreta)
    letras_adivinadas = []
    contador = 0

    while contador < 6 and palabra_usuario != palabra_secreta:
        print(ahorcado[contador])
        print("\nPalabra: " + " ".join(palabra_usuario))
        print("Letras usadas: " + ", ".join(letras_adivinadas))
        letra = input("Introduce una letra: ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print("⚠️ Por favor, introduce solo una letra.")
            continue

        if letra in letras_adivinadas:
            print("❗ Ya has dicho esa letra. Intenta con otra.")
            continue
        else:
            letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("✅ ¡Bien hecho! La letra está en la palabra.")
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    palabra_usuario[i] = letra
        else:
            contador += 1
            print(f"❌ La letra no está. Te quedan {6 - contador} vidas.")

        print("-" * 40)

    if contador == 6:
        print(ahorcado[6])
        print("💀 ¡Perdiste! La palabra era: " + "".join(palabra_secreta))
    else:
        print("🎉 ¡Felicidades! Has adivinado la palabra: " + "".join(palabra_usuario))
        print("🏆 ¡Eres un campeón!")
