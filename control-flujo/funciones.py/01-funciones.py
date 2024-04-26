def hola(nombre, apellido):  # parametros
    print("Hola mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola("Daniela", "Tangassi")  # argumentos
hola("Chanchito", "feliz")

# nombre de la variable dentro de la funcion eso es parametro


def hola(nombre, apellido="Feliz"):  # parametros
    print("Hola mundo!")
    print(f"Bienvenido {nombre} {apellido}")


hola("Daniela", "Tangassi")  # argumentos
hola("Chanchito")
# parametros opcionales

hola(apellido="Tangassi", nombre="Dani")
