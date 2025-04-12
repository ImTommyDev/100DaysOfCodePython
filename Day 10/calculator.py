print('''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculadora(num1, operacion, num2):
    if operacion == "+":
        return suma(num1, num2)
    elif operacion == "-":
        return resta(num1, num2)
    elif operacion == "*":
        return multiplicacion(num1, num2)
    elif operacion == "/":
        return division(num1, num2)
    else:
        return "Error: Invalid operation"
    

#Le pido al usuario que ingrese los numeros y la opreracion
num1 = float(input("Ingrese el primer número: "))
operacion = input("Ingrese la operación (+, -, *, /): ")
num2 = float(input("Ingrese el segundo número: "))

#Llamo a la funcion calculadora y le paso los argumentos
resultado = calculadora(num1, operacion, num2)
print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")

#Bucle, le pregunto al usuario si quiere hacer una operacion con el resultado obtenido
while True:
    continuar = input("¿Desea realizar otra operación con el resultado? (s/n): ")
    if continuar.lower() == 's':
        operacion = input("Ingrese la operación (+, -, *, /): ")
        num2 = float(input("Ingrese el segundo número: "))
        resultado = calculadora(resultado, operacion, num2)
        print(f"El resultado de {resultado} {operacion} {num2} es: {resultado}")
    else:
        print("Gracias por usar la calculadora.")
        break
#Fin del programa