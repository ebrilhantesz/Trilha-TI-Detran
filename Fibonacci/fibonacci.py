print("======================")
print("SEQUÊNCIA DE FIBONACCI")
print("======================")

while True:
    entrada = input("\nQuantos termos você deseja visualizar? ").strip()

    try:
        quantidade = int(entrada)
        if quantidade <= 0:
            print("Digite um número inteiro maior que zero.")
            continue
        break
    except ValueError:
        print("Entrada inválida! Digite apenas um número inteiro.")


# Lista
fibonacci = []
primeiro = 0
segundo = 1

for _ in range(quantidade):
    fibonacci.append(primeiro)
    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo


print("\n" + "=========")
print("RESULTADO")
print("=========")

print(f"\nQuantidade de termos: {quantidade}")
print(f"Sequência de Fibonacci: {fibonacci}")

print("\nPrograma encerrado.")