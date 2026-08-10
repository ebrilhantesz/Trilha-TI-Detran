# Ambiente Virtual e Variáveis de Ambiente em Python

Um projeto desenvolvido em **Python** para praticar a criação e utilização de um **ambiente virtual**, instalação de dependências, gerenciamento de **variáveis de ambiente** e configuração do **`.gitignore`** para proteger arquivos que não devem ser versionados.

---

## Tabela de Conteúdo

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Funciona](#como-funciona)
- [Como Executar](#como-executar)
- [Exemplo de Execução](#exemplo-de-execução)
- [Boas Práticas](#boas-práticas)
- [Autor](#autor)

---

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos relacionados ao gerenciamento de ambientes Python e à utilização de variáveis de ambiente.

O projeto cria um ambiente virtual isolado utilizando `venv`, instala as bibliotecas necessárias, armazena uma variável fictícia em um arquivo `.env` e utiliza Python para realizar a leitura dessa variável.

Também é utilizado um arquivo `.gitignore` para impedir que o ambiente virtual e o arquivo contendo as variáveis de ambiente sejam enviados para um repositório Git.

---

## Funcionalidades

- Criação de ambiente virtual com `venv`.
- Ativação do ambiente virtual.
- Instalação da biblioteca `requests`.
- Instalação da biblioteca `python-dotenv`.
- Criação e utilização de um arquivo `.env`.
- Leitura de variáveis de ambiente utilizando `os.getenv()`.
- Carregamento do `.env` utilizando `python-dotenv`.
- Criação de um arquivo `requirements.txt`.
- Configuração do `.gitignore`.
- Proteção do ambiente virtual e das variáveis de ambiente contra versionamento.

---

## Estrutura do Projeto

```text
desafio-venv/
│
├── venv/              # Ambiente virtual
│
├── .env               # Variáveis de ambiente
├── .gitignore         # Arquivos ignorados pelo Git
├── main.py            # Script principal
└── requirements.txt   # Dependências do projeto
```

> A pasta `venv/` e o arquivo `.env` não devem ser enviados para o repositório Git.

---

## Como Funciona

### 1. Ambiente Virtual

O ambiente virtual é criado com:

```bash
python -m venv venv
```

Ele cria um ambiente isolado para instalação das dependências do projeto.

---

### 2. Instalação das Dependências

Com o ambiente virtual ativado:

```bash
pip install requests python-dotenv
```

As dependências podem ser registradas em:

```bash
pip freeze > requirements.txt
```

---

### 3. Variável de Ambiente

O arquivo `.env` contém uma variável fictícia:

```env
API_KEY=12345
```

O arquivo é utilizado para armazenar configurações e informações que não devem ficar diretamente no código-fonte.

---

### 4. Leitura da Variável

O programa utiliza `python-dotenv` para carregar as informações do `.env`:

```python
from dotenv import load_dotenv

load_dotenv()
```

Depois, a variável pode ser recuperada utilizando:

```python
import os

api_key = os.getenv("API_KEY")
```

O programa verifica se a variável foi encontrada e informa o resultado.

---

### 5. Proteção com `.gitignore`

O arquivo `.gitignore` contém:

```gitignore
venv/
.env
__pycache__/
*.pyc
```

Dessa forma, arquivos e pastas que não devem ser versionados são ignorados pelo Git.

---

## Como Executar

### Pré-requisitos

- Python 3 instalado na máquina.
- Git instalado, caso o projeto seja versionado.

### Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/desafio-venv.git
```

### Acesse a pasta

```bash
cd desafio-venv
```

### Crie o ambiente virtual

```bash
python -m venv venv
```

### Ative o ambiente virtual

#### Windows — CMD

```cmd
venv\Scripts\activate
```

#### Windows — PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### Instale as dependências

```bash
pip install -r requirements.txt
```

### Execute o programa

```bash
python main.py
```

---

## Exemplo de Execução

```text
Variável API_KEY lida com sucesso!
```

Caso a variável não seja encontrada:

```text
A variável API_KEY não foi encontrada.
```

---

## Boas Práticas

### Não versionar o `.env`

O arquivo `.env` pode conter informações sensíveis, como:

- Chaves de API;
- Senhas;
- Tokens de autenticação;
- Credenciais de serviços.

Por isso, ele deve permanecer no `.gitignore`.

### Não versionar o ambiente virtual

A pasta `venv/` contém uma instalação local do Python e das dependências. Ela pode ser recriada utilizando:

```bash
python -m venv venv
```

As dependências do projeto devem ser compartilhadas através do arquivo:

```text
requirements.txt
```

---

## Autor

Desenvolvido por **Eduardo Henrique Brilhante**
