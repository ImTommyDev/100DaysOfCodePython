#Practicando para modificar una variable global
# Definimos una variable global
x = 5

# Definimos una función que modifica la variable global
def modificar_variable_global():
    global x  # Declaramos que vamos a usar la variable global x
    x = 10  # Modificamos la variable global
    print("Dentro de la función, x =", x)
    
# Llamamos a la función
modificar_variable_global()