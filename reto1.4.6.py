while True:
    try:
        primos = input("Ingresa una lista de números separados por espacios: ")
        lista = primos.split()
        if len(lista) < 2 or any(x.strip().isdigit() == False for x in lista):
            raise ValueError
        listap = [int(x) for x in lista]
        break
    except ValueError:
        print("Error: Debes ingresar al menos 2 números enteros separados por espacios.\n")

print(f"\nTu lista de numeros es: {listap}")

sum = 0
num = 0
num1 = 0
for i in range(len(listap) - 1):
    if listap[i] + listap[i + 1] > sum:
        sum = listap[i] + listap[i + 1]
        num = listap[i]
        num1 = listap[i + 1]
print(f"La suma mas grande de dos numeros consecutivos es: {num} + {num1} = {sum}")
