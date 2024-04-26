def suma(*numeros):  # fijarse en la identacion del for con el print
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 5, 7)  # iterable 2,5,7
suma(2, 5)
suma(2, 8, 7, 45, 32)
