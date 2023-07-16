'''
operadores de comparacion
igual a: ==
diferente de: !=
mayor que: >
maypr o igual que: >=
menor que: <
menor o igual: <=
'''

# ejemplo 1

numero = 2

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

print("------------------------")
# Ejemplo 2

fruta1 = "manzana"
fruta2 = "pera"

if fruta1 != fruta2:
    print("Las frutas son diferentes")
else:
    print("Las frutas son iguales")

print("------------------------")
# ejemplo 3

edad1 = 20
edad2 = 20

if edad1 > edad2:
    print("La primera persona es mayor")
elif edad1 < edad2:
    print("La segunda persona es mayor")
else:
    print("Ambas personas tienen la misma edad")
