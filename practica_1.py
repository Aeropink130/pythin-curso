'''
EN esta practica se evaluan 3 variables para saebr si:
todas son iguales
si 2 son iguales y una diferente
si todas son diferentes 
y cual es mayor
de igual manera se crea un fichero indicando el resultado
'''

# creamos el fichero escribiendo
# escribimos en el fichero lo que el programa hará
# -*- coding: utf-8 -*-


try:
    # acortamos la ruta ya que quiero que se cree en la carpeta en la que em encuentro
    fichero = open("fichero_practica_1.txt", "w", encoding="utf-8")
    fichero.write("Con este programa evaluamos las variables: \n")
    print("Fichero creado")
except FileNotFoundError:
    print("No se puede crar fichero")

# creamos las variables y el cuerpo del programa en un try para validar los valores
try:
    a = int(input("Escribe el numero a: "))
    b = int(input("Escribe el numero b: "))
    c = int(input("Escribe el numero c: "))

    fichero.write(f"variable a: {a}\nvariable b: {b}\nvariable c: {c}\n")

    if a == b == c:
        print("Los numeros son iguales")
        fichero.write("Los numeros son iguales\n")

    elif a == b and a != c:
        print("a y b son iguales y diferentes de c")
        fichero.write("a y b son iguales y diferentes de c\n1")
        if a > c:
            print(f"a y b ({a}) son mayores que c ({c})")
            fichero.write(f"a y b ({a}) son mayores que c ({c})\n")
        else:
            print(f"c ({c}) es mayor que a y b ({a})")
            fichero.write(f"c ({c}) es mayor que a y b ({a})\n")
    elif a == c and a != b:
        print("a y c son iguales b")
        fichero.write("a y c son iguales b\n")
        if a > b:
            print(f"a y c ({a}) son mayores que b ({b})")
            fichero.write(f"a y c ({a}) son mayores que b ({b})\n")
        else:
            print(f"b ({b}) es mayor que a y c ({a})")
            fichero.write(f"b ({b}) es mayor que a y c ({a})\n")
    elif b == c and b != a:
        print("b y c son iguales y diferentes de a")
        fichero.write("b y c son iguales y diferentes de a\n")
        if b > a:
            print(f"b y c ({b}) son mayores que a ({a})")
            fichero.write(f"b y c ({b}) son mayores que a ({a})\n")
        else:
            print(f"a ({a}) es mayor que b y c ({b})")
            fichero.write(f"a ({a}) es mayor que b y c ({b})\n")
    else:
        print("Todos los numeros son diferentes")
        fichero.write("Todos los numeros son diferentes\n")
        if a > b and a > c:
            print(f"a ({a}) es el numero mayor")
            fichero.write(f"a ({a}) es el numero mayor\n")
        elif b > a and b > c:
            print(f"b ({b}) es el numero mayor")
            fichero.write(f"b ({b}) es el numero mayor\n")
        else:
            print(f"C ({c}) es el numero mayor")
            fichero.write(f"C ({c}) es el numero mayor\n")


except ValueError as e:
    print("Escribe solo numero enteros")
    fichero.write("Error de valores\n")

finally:
    fichero.write("Fin")
    fichero.close()
