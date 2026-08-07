def coletar_notas():
    """Lê a quantidade de notas e os valores digitados com tratamento de erros."""
    while True:
        try:
            quantidade_notas = int(input("Quantas notas deseja inserir? "))
            if quantidade_notas > 0:
                break
            print("Por favor, informe uma quantidade maior que zero.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

    notas = []
    for i in range(quantidade_notas):
        while True:
            try:
                nota = float(input(f"Digite a nota {i + 1}: "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                print("A nota deve estar entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite um valor numérico.")
                
    return notas


def avaliar_desempenho(notas):
    """Calcula a média das notas e exibe o resultado final."""
    media = sum(notas) / len(notas)
    status = "Aprovado" if media >= 6.0 else "Reprovado"
    
    print(f"\nMédia final: {media:.2f}")
    print(f"Status: {status}")


def main():
    notas = coletar_notas()
    avaliar_desempenho(notas)

if __name__ == "__main__":
    main()