def saludar(nombre):
    """
    Función que saluda a la persona cuyo nombre se pasa como argumento.
    """
    print(f"Hola, {nombre}!")
    
def sumar(a, b):
    """
    Función que suma dos números y devuelve el resultado.
    """
    return a + b

def restar(a, b):
    """
    Función que resta dos números y devuelve el resultado.
    """
    return a - b

#Llamo a las funciones
saludar("Juan")
resultado_suma = sumar(5, 3)
print(f"La suma es: {resultado_suma}")
resultado_resta = restar(10, 4)
print(f"La resta es: {resultado_resta}")
