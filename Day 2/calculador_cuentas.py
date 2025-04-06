print("Bienvenido a la calculadora de cuentas")
multa = float(input("De cuanto ha sido la multa jefe?"))
propina = int(input("Cuanto es la propina jefe?")) #Integer (será un porcentaje)
personas = int(input("Cuantas personas son jefe?"))


total = multa + ( multa * (propina / 100))
print("El total por persona es: ", round(total / personas , 2))