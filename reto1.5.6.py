while True:
    try:
        entrada = input("Ingresa un grupo de palabras separadas por espacios: ")
        lista = entrada.split()
        if not lista or any(x.strip().isalpha() == False for x in lista):
            raise ValueError
        break
    except ValueError:
        print("Error: Ingresa solo palabras con letras, sin números ni símbolos.\n")

print(f"Tu lista de palabras es: {lista}")

usados = [False] * len(lista)
grupos = []

for i in range(len(lista)):
    if usados[i]:
        continue

    grupo = [lista[i]]
    usados[i] = True

    for j in range(i + 1, len(lista)):
        if not usados[j]:
            palabra1 = ''.join(sorted(lista[i].lower()))
            palabra2 = ''.join(sorted(lista[j].lower()))
            if palabra1 == palabra2:
                grupo.append(lista[j])
                usados[j] = True

    if len(grupo) > 1:
        grupos.append(grupo)

print("\nGrupos de anagramas encontrados:")
for grupo in grupos:
    print(grupo)
