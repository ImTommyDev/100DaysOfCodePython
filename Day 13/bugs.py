from random import randint

nombres = ["Tomas", "Juan", "Pedro", "Luis", "Maria"]

num_nombre = randint(0,6)

print("El nombre es: ", nombres[num_nombre]) #Genera el error index out of range porque el rango es de 0 a 5 y no de 0 a 6