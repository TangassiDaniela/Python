# and, or, not
# and dos condiciones, or
# not niega el resultado de una operacion

gas = False
encendido = True

if gas or encendido:
    print("Puedes avanzar")

gas = False
encendido = False

if not gas or encendido:
    print("Puedes avanzar")

gas = True
encendido = True
edad = 18
if gas and encendido and edad > 17:
    print("Puedes avanzar")

gas = False
encendido = True
edad = 18

if gas and (encendido or edad > 17):
    print("Puedes avanzar")

gas = False
encendido = True
edad = 18
if not gas and (encendido and edad > 17):
    print("Puedes avanzar")
