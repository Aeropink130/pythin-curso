# try...except

# podemos hacer uso e esta herramienta
# cuando se requiere validar un proceso
# si este coigo se ejecuta sin error
# continua con su ejecucion natural, pero si marca error
# se translada e inmediato a la parte de "except"

# ientacion: sangria o espacio que hay de izquierda a derecha
# es obligatorio en las estructuras logicas y ciertas herramientas

try:
    numero = int(input("Ingresa un número: "))
except ValueError:
    print("Ingresa un número baboso")
