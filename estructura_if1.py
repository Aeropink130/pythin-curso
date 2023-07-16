# estructura de control if
# La estructura e control if en python
# permite ejecutar bloques de codigo condicionalemnte

'''
En este tipo e estructuras tenemos una condicion
a evaluar, si resulta ser verdadero ingresa al cuerpo del 
if, de lo contrario no ingresa
'''

calificacion = 80

if calificacion >= 60:
    print("El estuiante aprobó prro")

cantidad = 99

# if con else

if cantidad > 100:
    print("Hay mas e 100 productos en el almacen")
else:
    print("No hay mas de 100 productos en el almacen")

# if elif y else
# Solo se puede tener un if, se pueden tener todos los elif que se necesiten y un solo else

n = float(input("Escribe el número: "))

if n > 0:
    print("El numero es positivo")
elif n < 0:
    print("El numero es negativo")
else:
    print("El número es 0")
