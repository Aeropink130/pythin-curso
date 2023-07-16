# importar una libreria
import os

# validar el proceso

try:
    # establecer la ruta del archivo
    archivo = open("C:\Python -19a21/archivo.txt    ", "w")

    archivo.write("Esta es la linea uno del archivo" + os.linesep)
    archivo.write("Esta es la linea dos del archivo" + os.linesep)
    archivo.write("Esta es la linea tres del archivo" + os.linesep)

    # cerrar archivo
    archivo.close()

    # avisar al usuario sobre la ejecucion
    print("se creo el archivo con exito")
except:
    print("error al crear el archivo")

try:
    archivo = open("C:\Python -19a21/archivo.txt    ", "r")
    print(archivo.read())
    archivo.close()
except:
    print("No esxite el pinche archivo")
