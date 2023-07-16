try:
    # recibir los datos a través de los input
    # se guardan en las variables e tipo float

    n1 = float(input("Escribe el primer número: "))
    n2 = float(input("Escribe el segundo número: "))

    # creamos las operaciones

    suma = n1+n2
    resta = n1-n2
    multi = n1*n2
    division = n1/n2

    # imprimir en la terminal

    print(f"suma: {suma}")
    print(f"resta: {resta}")
    print(f"multiplicacion: {multi}")
    print(f"division: {division}")

    # crear archivo
    # wt = escritura de texto universal
    archivo = open("C:\Python -19a21/archivo.txt", "w")

    # escribir sobre el archivo
    archivo.write("suma: " + str(suma) + "\n")
    archivo.write("resta: " + str(resta) + "\n")
    archivo.write("multiplicacion: " + str(multi) + "\n")
    archivo.write("division: " + str(division) + "\n")

except ValueError:
    print("Ingresasate un dato no válio baboso")
