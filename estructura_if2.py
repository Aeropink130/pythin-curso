try:
    monto = float(input("ingresa el monto de la compra: "))

    if monto > 1000:
        descuento = monto * 0.10
        total = monto - descuento
        print(f"El monto con escuento aplicado es: ${total}")
    elif monto > 900:
        descuento = monto * 0.09
        total = monto - descuento
        print(f"El monto con escuento aplicado es: ${total}")
    elif monto > 800:
        descuento = monto * 0.08
        total = monto - descuento
        print(f"El monto con escuento aplicado es: ${total}")
    elif monto > 700:
        descuento = monto * 0.07
        total = monto - descuento
        print(f"El monto con escuento aplicado es: ${total}")
    else:
        print(f"El monto total es: ${monto}")
except ValueError as e:
    print(f"Mugre perro, escribe el monto bien")
    print(e)

# elemplo 2

try:
    descuento = 0.0
    monto = float(input("ingresa el monto de la compra: "))

    if monto > 1000:
        descuento = monto * 0.10
        total = monto - descuento
    elif monto > 900:
        descuento = monto * 0.09
    elif monto > 800:
        descuento = monto * 0.08
    elif monto > 700:
        descuento = monto * 0.07
    else:
        print(f"El monto total es: ${monto}")

    total = monto - descuento
    print(f"El monto con escuento aplicado es: ${total}")

except ValueError as e:
    print(f"Mugre perro, escribe el monto bien")
    print(e)


# ejemplo 3
