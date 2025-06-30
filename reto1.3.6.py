while True:
    try:
        primos = input("Ingresa una lista de números separados por espacios: ")
        lista = primos.split()
        if not lista or any(x.strip().isdigit() == False for x in lista):
            raise ValueError
        listap = [int(x) for x in lista]
        break
    except ValueError:
        print("Error: Ingresa solo números enteros separados por espacios.\n")

print(f"\ntu lista de numeros es: {listap}")

cont = int
print("\nLos numeros primos de tu lista de numeros son")
for i in range(len(listap)):
    cont = 0
    for j in range(1, listap[i] + 1):
        if listap[i] % j == 0:
            cont += 1
    if cont == 2:
        print(listap[i])
