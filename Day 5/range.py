numeros = []
for number in range(1, 101):
    numeros.append(number)
    
print(numeros)

#Guardo el resultado en otra lista pero empezando por el 100
numeros_invertidos = []
for number in range(100, 0, -1):
    numeros_invertidos.append(number)
    
print(numeros_invertidos)

#Calculo cuanto es la suma de los numeros del 1 al 100
suma = 0
for turno in range(1,51):
    sum = numeros[turno] + numeros_invertidos[turno]
    suma += sum

print(suma)