try:
    a = int(input("Escribe el numero a: "))
    b = int(input("Escribe el numero b: "))
    c = int(input("Escribe el numero c: "))

    if a == b == c:
        print("Los numeros son iguales")

    elif a == b and a != c:
        print("a y b son iguales y diferentes de c")
        if a > c:
            print(f"a y b ({a}) son mayores que c ({c})")
        else:
            print(f"c ({c}) es mayor que a y b ({a})")
    elif a == c and a != b:
        print("a y c son iguales b")
        if a > b:
            print(f"a y c ({a}) son mayores que b ({b})")
        else:
            print(f"b ({b}) es mayor que a y c ({a})")
    elif b == c and b != a:
        print("b y c son iguales y diferentes de a")
        if b > a:
            print(f"b y c ({b}) son mayores que a ({a})")
        else:
            print(f"a ({a}) es mayor que b y c ({b})")
    else:
        print("Todos los numeros son diferentes")
        if a > b and a > c:
            print(f"a ({a}) es el numero mayor")
        elif b > a and b > c:
            print(f"b ({b}) es el numero mayor")
        else:
            print(f"C ({c}) es el numero mayor")


except ValueError as e:
    print("Escribe solo numero enteros")
    print(e)
