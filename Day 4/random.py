import random
import my_module

# Generar un número aleatorio entre el número definido en my_module y 15
entero_aleatorio = random.randint(my_module.numero, 15)
print(f"El número aleatorio es: {entero_aleatorio}")

# Generar un número floar aleatorio
float_aleatorio = random.uniform(0, 10)
print(f"El número float aleatorio es: {float_aleatorio}")