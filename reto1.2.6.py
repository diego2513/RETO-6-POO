while True:
    try:
        palabra = input("Ingresa una palabra: ")
        if palabra.strip() == "":
            raise ValueError("La palabra no puede estar vacía")
        if palabra.isalpha() == False:
            raise ValueError("La palabra solo puede contener letras")
        break
    except ValueError as e:
        print(f"Error: {e}\n")

palabra = palabra.lower()

for i in range(len(palabra)):
    if palabra[i] != palabra[-(i + 1)]:
        print(f"La palabra {palabra} no es un palindromo")
        break
else:
    print(f"La palabra {palabra} es un palindromo")
