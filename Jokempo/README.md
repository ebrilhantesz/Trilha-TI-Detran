
---

# Jokenpô em Python

Um jogo de **Jokenpô (Pedra, Papel e Tesoura)** desenvolvido em **Python**, executado via terminal. O usuário disputa partidas contra o computador, que realiza jogadas aleatórias. O programa mantém a pontuação durante toda a sessão e permite jogar quantas rodadas desejar.

---

## Tabela de Conteúdo

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Regras do Jogo](#regras-do-jogo)
- [Como Executar](#como-executar)
- [Exemplo de Execução](#exemplo-de-execução)
- [Autor](#autor)

---

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais da linguagem Python por meio da implementação de um jogo clássico.

Durante a execução, o jogador escolhe entre **Pedra**, **Papel** ou **Tesoura**, enquanto o computador realiza uma escolha aleatória. O programa compara as jogadas, informa o vencedor da rodada, atualiza a pontuação e oferece a possibilidade de continuar jogando.

---

## Funcionalidades

- Interface simples via terminal.
- Escolha entre Pedra, Papel ou Tesoura.
- Jogada aleatória do computador.
- Comparação automática das jogadas.
- Contagem de:
  - Vitórias do jogador;
  - Vitórias do computador;
  - Empates.
- Exibição da pontuação acumulada.
- Opção de continuar jogando ou encerrar a partida.
- Resultado final ao término do jogo.

---

## Regras do Jogo

| Jogada  | Vence   |
| ------- | ------- |
| Pedra   | Tesoura |
| Papel   | Pedra   |
| Tesoura | Papel   |

Se ambos os jogadores escolherem a mesma opção, a rodada termina em **empate**.

---

## Como Executar

### Pré-requisitos

- Python 3 instalado na máquina.

### Clone o repositório

```bash
git clone https://github.com/ebrilhantesz/Trilha-TI-Detran.git
```

### Acesse a pasta

```bash
cd jokenpo-python
```

### Execute o programa

```bash
python jokenpo.py
```

ou

```bash
python3 jokenpo.py
```

---

## Exemplo de Execução

```text
========================================
            JOKENPÔ
========================================

Escolha uma opção:
1 - Pedra
2 - Papel
3 - Tesoura
0 - Sair

Sua escolha: 2

Você escolheu: papel
Computador escolheu: pedra

Resultado: Você venceu!

Pontuação:
Você: 3
Computador: 1
Empates: 2

Deseja jogar novamente? (S/N): S
```

---

## Autor

Desenvolvido por **Eduardo Henrique Brilhante** 