# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes: (IMAGEN ADJUNTA).

# Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla lo que tiene que pagar.

def main():
    renta = int(input("Ingrese su renta anual: "))
    # renta = int(renta)

    if renta >= 0 and renta < 10000:
        total = renta * 0.05
    elif renta >= 10000 and renta < 20000:
        total = renta * 0.15
    elif renta >= 20000 and renta < 35000:
        total = renta * 0.2
    elif renta >= 35000 and renta < 60000:
        total = renta * 0.3
    elif renta >= 60000:
        total = renta * 0.45
    else:
        print("Valor no válido")

    print("Su impuesto es de: " + str(total))
    print("El total a pagar es: " + str(renta + total))
    


if __name__ == "__main__":
    main()
