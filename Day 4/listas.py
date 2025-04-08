#Creando una lista con los estados de america por orden de alfabeto
estados_america = ["Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas",
"Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri"]

#Obtengo el primero
print(estados_america[0])

#Obtengo el ultimo
print(estados_america[-1])

#Cambio el significado del segundo
estados_america[1] = "Alabama"
print(estados_america[1])

#Añado uno
estados_america.append("Alaska")
print(estados_america[-1])

#Añado varios
estados_america.extend(["Arkansas","California","Colorado","Connecticut","Delaware"])
print(estados_america[-1])

#Creando una lista de listas
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1]) # Kale (coge el segundo elemento de la segunda lista)