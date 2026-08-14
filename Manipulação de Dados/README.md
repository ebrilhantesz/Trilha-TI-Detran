# Manipulação de Dados com Google Sheets, Pandas e Python

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-DataFrame-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Google Sheets](https://img.shields.io/badge/Google%20Sheets-API-34A853?style=for-the-badge&logo=googlesheets&logoColor=white)
![gspread](https://img.shields.io/badge/gspread-Google%20Sheets-4285F4?style=for-the-badge&logo=google&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-2ea44f?style=for-the-badge)

Projeto desenvolvido em **Python** para praticar integração com o **Google Sheets**, leitura de dados utilizando **gspread**, manipulação com **Pandas** e atualização automática de uma segunda aba da mesma planilha.

---

## Tabela de Conteúdo

- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivos](#objetivos)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Funcionamento](#funcionamento)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Configuração](#configuração)
- [Variáveis de Ambiente](#variáveis-de-ambiente)
- [Instalação](#instalação)
- [Execução](#execução)
- [Fluxo do Programa](#fluxo-do-programa)
- [Resultado](#resultado)
- [Segurança](#segurança)
- [Aprendizados](#aprendizados)
- [Repositório](#repositório)
- [Autor](#autor)

---

## Sobre o Projeto

O objetivo deste exercício é desenvolver um programa capaz de acessar uma planilha do **Google Sheets**, carregar seus dados para um **DataFrame do Pandas**, identificar os alunos que possuem status **Pendente** e escrever automaticamente esse resultado em uma segunda aba da mesma planilha.

O projeto foi desenvolvido inicialmente no **Jupyter Notebook**, permitindo testar cada etapa individualmente. Após a validação, a solução foi organizada em um programa Python (`main.py`) com funções separadas para cada responsabilidade.

---

## Objetivos

O programa realiza três operações principais:

1. Conecta-se ao Google Sheets utilizando uma **Service Account**.
2. Lê os dados da aba principal e transforma as informações em um DataFrame do Pandas.
3. Filtra somente os alunos com status `Pendente`.
4. Cria ou localiza uma segunda aba chamada `Pendentes`.
5. Atualiza essa segunda aba com o resultado filtrado.

---

## Tecnologias Utilizadas

- **Python**
- **Pandas**
- **gspread**
- **python-dotenv**
- **Google Sheets**
- **Google Service Account**
- **Jupyter Notebook**
- **VS Code**

| Biblioteca | Utilização |
|---|---|
| `gspread` | Conexão e manipulação do Google Sheets |
| `pandas` | Criação e manipulação do DataFrame |
| `python-dotenv` | Leitura das variáveis do `.env` |
| `os` | Variáveis de ambiente e caminhos |

---

## Funcionamento

A planilha possui uma aba principal chamada `teste_alunos`, com as colunas:

```text
Nome
Curso
Status
```

O programa lê os dados:

```python
dados_puros = aba.get_all_values()
```

e transforma o conteúdo em um DataFrame:

```python
df = pd.DataFrame(
    dados_puros[1:],
    columns=dados_puros[0]
)
```

Depois verifica a coluna `Status` e filtra os alunos pendentes:

```python
pendentes = df[df["Status"] == "Pendente"]
```

Por fim, os registros são gravados em uma segunda aba chamada `Pendentes`.

---

## Estrutura do Projeto

```text
Manipulação de Dados/
│
├── main.py
├── main.ipynb
├── .env
├── .gitignore
└── credenciais_google.json
```

| Arquivo | Descrição |
|---|---|
| `main.py` | Programa Python principal |
| `main.ipynb` | Notebook utilizado para testes |
| `.env` | Variáveis de configuração |
| `.gitignore` | Arquivos que não devem ser versionados |
| `credenciais_google.json` | Credenciais da Service Account |

> **Importante:** o arquivo de credenciais não deve ser enviado para o GitHub.

---

## Configuração

É necessário possuir:

- Python instalado;
- Uma Google Service Account;
- Arquivo JSON das credenciais;
- Uma planilha do Google Sheets;
- Permissão da Service Account para acessar a planilha.

A planilha deve ser compartilhada com o e-mail da Service Account.

---

## Variáveis de Ambiente

O projeto utiliza `.env` para armazenar configurações.

Exemplo:

```env
GOOGLE_CREDENTIALS_PATH=C:/caminho/para/credenciais_google.json
```

Em ambientes com proxy, também podem ser utilizadas:

```env
HTTP_PROXY=http://seu-proxy:porta
HTTPS_PROXY=http://seu-proxy:porta
NO_PROXY=
```

O programa carrega essas informações com:

```python
from dotenv import load_dotenv

load_dotenv()
```

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/ebrilhantesz/Trilha-TI-Detran.git
```

Acesse a pasta:

```bash
cd Trilha-TI-Detran
```

Instale as dependências:

```bash
pip install pandas gspread python-dotenv
```

---

## Execução

Execute:

```bash
python main.py
```

O programa irá:

```text
1. Carregar as configurações
2. Localizar as credenciais
3. Conectar ao Google Sheets
4. Abrir "teste_alunos"
5. Ler os dados
6. Criar o DataFrame
7. Filtrar os alunos pendentes
8. Criar/localizar a aba "Pendentes"
9. Limpar dados anteriores
10. Gravar os dados atualizados
```

---

## Fluxo do Programa

```text
                GOOGLE SHEETS
                      │
                      ▼
                teste_alunos
                      │
                      ▼
                   gspread
                      │
                      ▼
                DataFrame
                      │
                      ▼
             Status == "Pendente"
                      │
                      ▼
              DataFrame filtrado
                      │
                      ▼
                Aba Pendentes
                      │
                      ▼
                GOOGLE SHEETS
```

---

## Resultado

### Aba `teste_alunos`

| Nome | Curso | Status |
|---|---|---|
| Eduardo Brilhante | Python | Concluído |
| Douglas Ribeiro | Pandas | Pendente |
| Caio Santos | Python | Concluído |
| Mary Hellen | Google Sheets | Pendente |
| Marcel Costa | Python | Concluído |
| Everton Quadros | Pandas | Pendente |

### Aba `Pendentes`

| Nome | Curso | Status |
|---|---|---|
| Douglas Ribeiro | Pandas | Pendente |
| Mary Hellen | Google Sheets | Pendente |
| Everton Quadros | Pandas | Pendente |

A aba `Pendentes` é limpa antes da atualização:

```python
aba_pendentes.clear()
```

Assim, registros antigos não permanecem no relatório quando a quantidade de pendências muda.

---

## Organização do Código

O `main.py` foi dividido em funções:

### `carregar_configuracoes()`

Carrega o `.env`, configura o proxy e valida o caminho das credenciais.

### `conectar_google_sheets()`

Realiza a autenticação utilizando a Service Account.

### `ler_planilha()`

Abre a planilha, lê a primeira aba e cria o DataFrame.

### `filtrar_pendentes()`

Valida a coluna `Status` e retorna somente os registros pendentes.

### `escrever_pendentes()`

Cria ou localiza a aba `Pendentes`, limpa os dados anteriores e grava o resultado.

### `main()`

Coordena todo o fluxo do programa.

---

## Segurança

O arquivo de credenciais e o `.env` não devem ser publicados no GitHub.

Exemplo de `.gitignore`:

```gitignore
.env
*.json
__pycache__/
*.pyc
```

**Nunca publique o arquivo JSON da Service Account no repositório.**

---

## Aprendizados

Este projeto permitiu praticar:

- Integração entre Python e Google Sheets;
- Autenticação com Service Account;
- Utilização do `gspread`;
- Leitura de dados externos;
- Criação e manipulação de DataFrames;
- Filtragem de dados;
- Validação de colunas;
- Criação e atualização de abas;
- Uso de variáveis de ambiente;
- Organização de código em funções;
- Desenvolvimento e testes com Jupyter Notebook;
- Boas práticas básicas de segurança.

---

## Repositório

O projeto faz parte do repositório:

**[Trilha-TI-Detran](https://github.com/ebrilhantesz/Trilha-TI-Detran)**

---

## Autor

Desenvolvido por **Eduardo Henrique Brilhante**

---

<p align="center">
  Desenvolvido com Python, Pandas e Google Sheets.
</p>
