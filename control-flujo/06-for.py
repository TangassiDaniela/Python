for numero in range(5):
    # identado un poco el codigo
    # range 5 crea una secuencia de numeros que se podra usar dentro de for 0,1,2,3,4
    print(numero, numero * "hola mundo")

buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break

buscar = 10
for numero in range(5):  # es una iterable, hay listas y tuplas
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontre el numero buscado")

for char in "ultimate python":
    print(char)
