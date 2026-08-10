# Sequência de Fibonacci em Python

Um programa desenvolvido em **Python** que solicita ao usuário a quantidade de termos desejada e gera a **sequência de Fibonacci** na ordem correta. O programa também realiza a validação da entrada para evitar valores inválidos.

---

## Tabela de Conteúdo

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Como Funciona](#como-funciona)
- [Como Executar](#como-executar)
- [Exemplo de Execução](#exemplo-de-execução)
- [Autor](#autor)

---

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais da linguagem Python, como estruturas de repetição, variáveis, listas, operadores matemáticos e validação de entrada de dados.
Durante a execução, o usuário informa quantos termos deseja visualizar. O programa então calcula e apresenta a sequência de Fibonacci na ordem correta.
A sequência começa com **0 e 1**, sendo que cada termo seguinte é obtido pela soma dos dois termos anteriores.

---

## Funcionalidades

- Interface simples via terminal.
- Solicitação da quantidade de termos desejada.
- Validação de entradas inválidas.
- Validação para impedir números menores ou iguais a zero.
- Geração automática da sequência de Fibonacci.
- Exibição da quantidade de termos solicitada.
- Exibição da sequência completa.

---

## Como Funciona

1. O programa solicita ao usuário a quantidade de termos desejada.
2. A entrada é validada para garantir que seja um número inteiro positivo.
3. A sequência começa com os valores `0` e `1`.
4. O programa calcula cada novo termo somando os dois termos anteriores.
5. O processo é repetido até atingir a quantidade solicitada.
6. Ao final, a sequência completa é exibida no terminal.

### Exemplo da sequência

Para **10 termos**:

```text
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

Cada termo é calculado da seguinte forma:

```text
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
...
```

---

## Como Executar

### Pré-requisitos

- Python 3 instalado na máquina.

### Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/fibonacci-python.git
```

### Acesse a pasta

```bash
cd fibonacci-python
```

### Execute o programa

```bash
python fibonacci.py
```

ou

```bash
python3 fibonacci.py
```

---

## Exemplo de Execução

```text
======================
SEQUÊNCIA DE FIBONACCI
======================

Quantos termos você deseja visualizar? 10

=========
RESULTADO
=========

Quantidade de termos: 10
Sequência de Fibonacci: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

Programa encerrado.
```

### Exemplo de entrada inválida

```text
Quantos termos você deseja visualizar? abc

Entrada inválida! Digite apenas um número inteiro.

Quantos termos você deseja visualizar? -5

Digite um número inteiro maior que zero.

Quantos termos você deseja visualizar? 8

=========
RESULTADO
=========

Quantidade de termos: 8
Sequência de Fibonacci: [0, 1, 1, 2, 3, 5, 8, 13]
```

---

## Autor

Desenvolvido por **Eduardo Henrique Brilhante**