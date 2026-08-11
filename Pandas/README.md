# Relatório de Pendências de Funcionários em Python

Um programa desenvolvido em **Python** utilizando a biblioteca **Pandas** para criar uma tabela de funcionários, identificar aqueles que possuem status **Pendente** e gerar automaticamente um relatório em formato Excel.

---

## Tabela de Conteúdo

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Funciona](#como-funciona)
- [Como Executar](#como-executar)
- [Exemplo de Execução](#exemplo-de-execução)
- [Resultado](#resultado)
- [Autor](#autor)

---

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar o uso da biblioteca **Pandas** para manipulação e filtragem de dados.

O programa cria um `DataFrame` contendo informações de funcionários, como **Nome, CPF e Status**. Em seguida, realiza um filtro para identificar somente os funcionários que possuem o status **Pendente**.

Os dados filtrados são então exportados para um arquivo Excel chamado:

```text
relatorio_pendencias.xlsx
```

---

## Funcionalidades

- Criação de um `DataFrame` utilizando Pandas.
- Cadastro de funcionários.
- Armazenamento das informações:
  - Nome;
  - CPF;
  - Status.
- Filtragem dos funcionários com status `Pendente`.
- Exibição do DataFrame completo no terminal.
- Exibição dos funcionários com pendências.
- Exportação do resultado para um arquivo Excel.
- Geração automática do arquivo `relatorio_pendencias.xlsx`.

---

## Estrutura do Projeto

```text
Relatorio de Pendencias/
│
├── relatorio_pendencias.py
└── relatorio_pendencias.xlsx
```

O arquivo Excel é criado automaticamente após a execução do programa.

---

## Como Funciona

### 1. Criação dos dados

O programa cria um conjunto de dados contendo três colunas:

```text
Nome
CPF
Status
```

Exemplo:

```text
Nome             CPF              Status
Ana Souza        123.456.789-00   Regular
Carlos Lima      987.654.321-00   Pendente
Mariana Silva    456.789.123-00   Regular
```

### 2. Criação do DataFrame

Os dados são transformados em um `DataFrame` utilizando:

```python
df = pd.DataFrame(funcionarios)
```

O `DataFrame` permite trabalhar com os dados de forma semelhante a uma tabela.

### 3. Filtragem das pendências

O programa utiliza uma condição para manter somente os funcionários cujo status seja `Pendente`:

```python
pendencias = df[df["Status"] == "Pendente"]
```

### 4. Exportação para Excel

O resultado filtrado é salvo utilizando:

```python
pendencias.to_excel("relatorio_pendencias.xlsx", index=False)
```

O parâmetro `index=False` impede que o índice interno do Pandas seja incluído como uma coluna no arquivo Excel.

---

## Como Executar

### Pré-requisitos

- Python 3 instalado na máquina.
- Pandas instalado.
- OpenPyXL instalado para permitir a criação do arquivo Excel.

### Instale as dependências

```bash
pip install pandas openpyxl
```

### Clone o repositório

```bash
git clone https://github.com/ebrilhantesz/Trilha-TI-Detran.git
```

### Acesse a pasta

```bash
cd "Relatorio de Pendencias"
```

### Execute o programa

```bash
python relatorio_pendencias.py
```

ou:

```bash
python3 relatorio_pendencias.py
```

---

## Exemplo de Execução

```text
========================================
RELATÓRIO DE PENDÊNCIAS
========================================

DataFrame completo:
            Nome               CPF     Status
0      Ana Souza  123.456.789-00    Regular
1    Carlos Lima  987.654.321-00  Pendente
2  Mariana Silva  456.789.123-00    Regular

Funcionários com pendências:
          Nome               CPF     Status
1  Carlos Lima  987.654.321-00  Pendente

Arquivo 'relatorio_pendencias.xlsx' criado com sucesso!
```

---

## Resultado

Após a execução, será criado o arquivo:

```text
relatorio_pendencias.xlsx
```

O arquivo conterá somente os funcionários que possuem pendências:

| Nome | CPF | Status |
|---|---|---|
| Carlos Lima | 987.654.321-00 | Pendente |

Esse relatório pode ser aberto normalmente no **Microsoft Excel**, LibreOffice Calc ou outro programa compatível com arquivos `.xlsx`.

---

## Autor

Desenvolvido por **Eduardo Henrique Brilhante** como atividade prática para aplicação dos conceitos fundamentais de **Pandas, DataFrames, filtragem de dados e exportação para Excel em Python**.
