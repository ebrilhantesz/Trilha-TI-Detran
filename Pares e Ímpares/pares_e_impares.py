# Listas
numeros = []
pares = []
impares = []

print("============================")
print("SEPARADOR DE PARES E ÍMPARES")
print("============================")

while True:
    entrada = input("\nDigite um número inteiro (ou 'F' para finalizar): ").strip().upper()

    if entrada == "F":
        break
    try:
        numero = int(entrada)
    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros ou 'F' para finalizar.")
        continue

    numeros.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\n" + "=====================")
print("RESULTADO")
print("=====================")

print(f"Lista completa: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")

print("\nPrograma encerrado.")