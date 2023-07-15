#python es un leguaje de tipado dinámico

'''
indica que sus variables pueden tomar difarentes
tipos de dato en tienpo de ejecucion, es decir
cambiar el tipo de valor que almacena

por lo tanto en python no es obligatorio señalar el tipo de dato
que almacenará la variable
'''
#sin especificar el tipo de dato
nombre = "Antonio"
edad = 28
altura = 1.76
estudiante = True


#especificando el tipo de dato a almacenar
nombre =  str("Antonio")
edad = int(28)
altura = float(1.76)
estudiante = bool(True)

print("Mi nombre es: ", nombre)
print("Mi edad es: ", edad)
print("Mi altura es es: ", altura)
print("Estuiante: ", estudiante)
