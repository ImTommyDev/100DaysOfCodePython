import random

print("Bienvenido al generador de contraseñas")
letras = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
         "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
         "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

simbolos = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

letras_deseadas = int(input("¿Cuántas letras quieres en tu contraseña?\n"))
numeros_deseados = int(input("¿Cuántos números quieres en tu contraseña?\n"))
simbolos_deseados = int(input("¿Cuántos símbolos quieres en tu contraseña?\n"))

#Generar la contraseña
#Lo primero que voy a hacer es crear una lista vacía donde voy a guardar los caracteres
contraseña = []

#Voy a usar un bucle for para añadir las letras, números y símbolos a la lista
for letra in range(1, letras_deseadas + 1):
    contraseña.append(random.choice(letras))
for numero in range(1, numeros_deseados + 1):
    contraseña.append(random.choice(numeros))
for simbolo in range(1, simbolos_deseados + 1):
    contraseña.append(random.choice(simbolos))
    
#Mezclar la contraseña
random.shuffle(contraseña)

#Convertir la lista en string
contraseña_final = ""
for char in contraseña:
    contraseña_final += char
    
print(f"Tu contraseña es: {contraseña_final}")