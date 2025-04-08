import random

eleccion = input("¿Cara o cruz pichita? (C/T): ").upper()
while eleccion not in ["C", "T"]:
    eleccion = input("Opcion no valida payaso, elige entre C o T: ").upper()

resultado = random.choice(["C", "T"])

if eleccion == resultado:
    print(f'El resultado es {resultado} ¡Ganaste!')
else:
    print(f'El resultado es {resultado} Perdiste! (jodete)')