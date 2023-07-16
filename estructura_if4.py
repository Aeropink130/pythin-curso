'''
operadores logicos
Y: AND
O: Or
No: Not
'''

# ejemplo  1

edad = 13

if edad < 13:
    print("es un niño/niña")
elif edad >= 13 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad <= 60:
    print("Adulto")
else:
    print("Adulto mayor")

print("------------------------")
# ejemplo 2

x = False
y = False
z = False

if x == True or y == True or z == True:
    print("La hipotesis es verdadera")
else:
    print("La hipotesis es falsa")

print("------------------------")
# ejemplo 3

opcion = 1

if not opcion == 0:
    print("La opcion es válida (diferente de 0)")

print("------------------------")
# ejemplo 4

letra = "a"
palabra = "viernes"

if letra not in palabra:
    print(f"La letra {letra} no está en la palabra {palabra}")
else:
    print(f"La letra {letra} sí está en la palabra {palabra}")

print("------------------------")
# Ejemplo 5

sabor = "gansito"
sabores = ["chocolate", "vainilla", "fresa", "nuez"]

if sabor in sabores:
    print(f"sí hay {sabor}")
else:
    print(f"no hay {sabor}")
