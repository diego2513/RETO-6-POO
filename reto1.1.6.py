while True:
    try:
        numero1 = int(input("Ingrese el numero 1: "))
        numero2 = int(input("Ingrese el numero 2: "))
        break
    except ValueError:
        print("Error: Debes ingresar números enteros válidos.")

opcion = str

while opcion != "!":
    print("\n+------------------------------------+")
    print("+               MENU                 +")
    print("+ 1. SUMAR LOS DOS NUMEROS  (+)      +")
    print("+ 2. RESTAR LOS DOS NUMEROS (-)      +")
    print("+ 3. DIVIDIR LOS DOS NUMEROS (/)     +")
    print("+ 4. SUMAR LOS DOS NUMEROS (*)       +")
    print("+ 5. SALIR (!)                        +")
    print("+------------------------------------+")
    opcion = input("\nIngrese la opcion de su preferencia: ")

    while opcion not in ["+", "-", "/", "*", "!"]:
        opcion = input("\nOpcion no valida, ingresa de nuevo una opcion: ")

    if opcion == "+":
        print(f"\nLa suma de los numeros es {numero1 + numero2}")

    elif opcion == "-":
        print(f"\nEl numero 1 - el numero 2 es {numero1 - numero2}")
        print(f"\nEl numero 2 - el numero 1 es {numero2 - numero1}")

    elif opcion == "*":
        print(f"\nLa multiplicacion de los numeros es {numero1 * numero2}")

    elif opcion == "/":
        try:
            print(f"\nEl numero 1 / numero 2 es {numero1 / numero2}")
        except ZeroDivisionError:
            print("\nError: No se puede dividir el número 1 entre cero.")

        try:
            print(f"\nEl numero 2/numero 1 es {numero2 / numero1}")
        except ZeroDivisionError:
            print("\nError: No se puede dividir el número 2 entre cero.")

    else:
        print("\nHas salido") 
        break
