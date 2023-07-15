# repaso 1

'''
Variables
Operadores aritmeticos
Try.. except
Ientacion
Fichero
'''
# Delcaracion de variables de manera explicita

# preguntar sobre imports cuando usar from
from datetime import *

# preguntar sobre convensiones
producto = str("computadora")
cantidad = int(100)
precio = float(16000.99)
disponible = bool(True)
fecha_ingreso = date(2023, 7, 13)
hora_ingreso = time(19, 00, 00)

# declaracion de variables con tipado dinamico

producto = "computadora"
cantidad = 100
precio = 16000.99
disponible = True
fecha_ingreso = "2023-7-13"
hora_ingreso = "19:00:00"

# operadores aritmeticos

suma = 10 + 10
resta = 10-5
multi = 3*6
division = 10/3
division_entera = 10//3  # division entera
modulo = 10 % 3  # residuo de la division
potencia = 2**2

# identacion: en python se refiere al espacio o sangria que se
# utiliza para estructurar y organizar  el codigo

try:
    # intenta realizar lo siguiente
    contraseña = int(input("escribe la contraseña numerica"))
    print(f"La contraseña es: {contraseña}")

    try:
        pass
    except:
        pass
except ValueError as error:
    # si lo anterior genera error entonces:
    print("Dato invalido baboso")
    print(error)
# except Exception as error:
#     print("Hiciste algo mal mi chavo")
#     print(error)
