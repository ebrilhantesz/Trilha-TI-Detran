# Separador de Números Pares e Ímpares em Python

Um programa desenvolvido em **Python** que recebe uma sequência de números inteiros informados pelo usuário, separando-os automaticamente em duas listas: uma contendo os números **pares** e outra contendo os **ímpares**. Ao final da execução, o programa exibe todas as listas geradas.

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

Este projeto foi desenvolvido com o objetivo de praticar conceitos fundamentais da linguagem Python, como estruturas de repetição, listas, estruturas condicionais e validação de entrada de dados.

Durante a execução, o usuário pode informar quantos números inteiros desejar. O programa verifica automaticamente se cada número é par ou ímpar, armazenando-o na lista correspondente. Ao finalizar a entrada de dados, todas as listas são apresentadas ao usuário.

---

## Funcionalidades

- Interface simples via terminal.
- Entrada de uma quantidade ilimitada de números inteiros.
- Validação de entradas inválidas.
- Separação automática entre números pares e ímpares.
- Armazenamento dos números em listas.
- Exibição da:
  - Lista completa;
  - Lista de números pares;
  - Lista de números ímpares.
- Encerramento do programa mediante comando do usuário.

---

## Como Funciona

1. O usuário informa um número inteiro.
2. O programa verifica se o número é par ou ímpar.
3. O número é armazenado na lista correspondente.
4. O processo se repete até que o usuário digite **F** para finalizar.
5. Ao final, o programa exibe todas as listas geradas.

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
cd pares-impares-python
```

### Execute o programa

```bash
python pares_impares.py
```

ou

```bash
python3 pares_impares.py
```

---

## Exemplo de Execução

```text
========================================
     SEPARADOR DE PARES E ÍMPARES
========================================

Digite um número inteiro (ou 'F' para finalizar): 10

Digite um número inteiro (ou 'F' para finalizar): 7

Digite um número inteiro (ou 'F' para finalizar): 18

Digite um número inteiro (ou 'F' para finalizar): 5

Digite um número inteiro (ou 'F' para finalizar): 0

Digite um número inteiro (ou 'F' para finalizar): F

========================================
RESULTADO
========================================

Lista completa: [10, 7, 18, 5, 0]
Números pares: [10, 18, 0]
Números ímpares: [7, 5]

Programa encerrado.
```

---

## Autor

Desenvolvido por **Eduardo Henrique Brilhante**