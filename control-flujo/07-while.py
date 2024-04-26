# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2

comando = None  # Inicializa comando como None en lugar de una cadena vacía

while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
