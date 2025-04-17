import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_moneda(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada.isdigit():
            return int(entrada)
        else:
            print("⚠️  Por favor, introduce un número válido.")
