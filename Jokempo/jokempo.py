import random

# Pontuação
jogador = 0
computador = 0
empates = 0

opcoes = ["pedra", "papel", "tesoura"]

print("===============")
print("    JOKENPÔ")
print("===============")

while True:
    print("\nEscolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    print("0 - Sair")

    escolha = input("Sua escolha: ")

    if escolha == "0":
        break
    if escolha not in ["1", "2", "3"]:
        print("Opção inválida! Tente novamente.")
        continue

    jogador_escolha = opcoes[int(escolha) - 1]
    computador_escolha = random.choice(opcoes)

    print(f"\nVocê escolheu: {jogador_escolha}")
    print(f"Computador escolheu: {computador_escolha}")

    if jogador_escolha == computador_escolha:
        print("Resultado: Empate!")
        empates += 1
    elif (
        (jogador_escolha == "pedra" and computador_escolha == "tesoura") or
        (jogador_escolha == "papel" and computador_escolha == "pedra") or
        (jogador_escolha == "tesoura" and computador_escolha == "papel")
    ):
        print("Resultado: Você venceu!")
        jogador += 1
    else:
        print("Resultado: Computador venceu!")
        computador += 1

    print("\nPontuação:")
    print(f"Você: {jogador}")
    print(f"Computador: {computador}")
    print(f"Empates: {empates}")

    while True:
        continuar = input("\nDeseja jogar novamente? (S/N): ").strip().upper()
        if continuar in ["S", "N"]:
            break
        else:        
            print("\nOpção inválida! Digite apenas S para Sim ou N para Não.")
    if continuar == "N":
            break

print("\n" + "===============")
print("  FIM DO JOGO")
print("===============")
print(f"Vitórias do jogador: {jogador}")
print(f"Vitórias do computador: {computador}")
print(f"Empates: {empates}")

if jogador > computador:
    print("Parabéns! Você venceu a partida!")
elif computador > jogador:
    print("O computador venceu a partida!")
else:
    print("A partida terminou empatada!")
print("Obrigado por jogar!")