#declarar las variables

nombre = "AntOniO SalCiDO"
minusculas = nombre.lower()
mayusculas = nombre.upper()
propio = nombre.title()

'''
imprimir concatenando con la coma ","
'''
print("Nombre normal: ", nombre)
print("Nombre minusculas: ", minusculas)
print("Nombre normal: ", mayusculas)
print("Nombre propio: ", propio)

print("------------------------")

'''
imprimir concatenando con el "+"
'''

print("Nommbre normal: " + nombre)
print("Nommbre minusculas: " + minusculas)
print("Nommbre mayusculas: " + mayusculas)
print("Nommbre propio: " + propio)

print("------------------------")

'''
imprimir concatenando con f
'''

print(f"nombre normal: {nombre}")
print(f"nombre minusculas: {minusculas}")
print(f"nombre mayusculas: {mayusculas}")
print(f"nombre propio: {propio}")