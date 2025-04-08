import random

print("Bienvenido al juego de piedra, papel o tijera")
print("Elige una opción:")
print("1. Piedra")
print("2. Papel")
print("3. Tijera")

piedra = '''
(__)
'''
papel = '''
[__]
'''
tijera = '''
 X
/ \
'''

eleccion_usuario = int(input("Ingresa el número de tu elección: "))

while eleccion_usuario not in [1, 2, 3]:
    eleccion_usuario = int(input("Ingresa el número de tu elección nuevamente tramposillo: "))
    
eleccion_rival = random.randint(1, 3)

if eleccion_usuario == 1:
    print(f"Tu elección: \n{piedra}")
    if eleccion_rival == 1:
        print(f"Elección del rival: \n{piedra}")
        print("Empate")
    elif eleccion_rival == 2:
        print(f"Elección del rival: \n{papel}")
        print("Perdiste")
    else:
        print(f"Elección del rival: \n{tijera}")
        print("Ganaste")
elif eleccion_usuario == 2:
    print(f"Tu elección: \n{papel}")
    if eleccion_rival == 1:
        print(f"Elección del rival: \n{piedra}")
        print("Ganaste")
    elif eleccion_rival == 2:
        print(f"Elección del rival: \n{papel}")
        print("Empate")
    else:
        print(f"Elección del rival: \n{tijera}")
        print("Perdiste")
else:
    print(f"Tu elección: \n{tijera}")
    if eleccion_rival == 1:
        print(f"Elección del rival: \n{piedra}")
        print("Perdiste")
    elif eleccion_rival == 2:
        print(f"Elección del rival: \n{papel}")
        print("Ganaste")
    else:
        print(f"Elección del rival: \n{tijera}")
        print("Empate")
        