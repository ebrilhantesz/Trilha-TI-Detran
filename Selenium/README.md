# Consulta de CPF com Selenium

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Automation-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![WebDriver](https://img.shields.io/badge/WebDriver-Chrome-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Local%20Page-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-2ea44f?style=for-the-badge)

Projeto desenvolvido em **Python** para praticar automação de navegador utilizando **Selenium WebDriver**, abertura de arquivos HTML locais, preenchimento automático de campos, interação com botões e captura de resultados utilizando esperas explícitas.

---

## Tabela de Conteúdo

- [Sobre o Projeto](#sobre-o-projeto)
- [Objetivos](#objetivos)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Funcionamento](#funcionamento)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Configuração](#configuração)
- [Instalação](#instalação)
- [Execução](#execução)
- [Fluxo do Programa](#fluxo-do-programa)
- [Resultado](#resultado)
- [Organização do Código](#organização-do-código)
- [Repositório](#repositório)
- [Autor](#autor)

---

## Sobre o Projeto

O objetivo deste exercício é desenvolver um programa capaz de acessar um arquivo **HTML local** que simula um sistema de consulta de CPF, preencher automaticamente um CPF de teste, realizar a consulta e capturar o resultado exibido na tela.
O projeto foi desenvolvido inicialmente no **Jupyter Notebook**, permitindo testar cada etapa individualmente. Após a validação, a solução foi organizada em um programa Python (`consulta_selenium.py`) com funções separadas para cada responsabilidade.
Os dados utilizados no sistema são fictícios e destinados exclusivamente ao ambiente de treinamento.

---

## Objetivos

O programa realiza as seguintes operações:

1. Abre o Google Chrome utilizando Selenium WebDriver.
2. Localiza e abre o arquivo `consulta_cpf.html`.
3. Localiza o campo de CPF.
4. Preenche um CPF de teste.
5. Localiza e aciona o botão `Consultar`.
6. Aguarda o carregamento do resultado utilizando `WebDriverWait`.
7. Captura o conteúdo exibido no elemento de resultado.
8. Imprime o resultado no terminal.
9. Fecha o navegador ao final da execução.

---

## Tecnologias Utilizadas

- **Python**
- **Selenium**
- **Chrome WebDriver**
- **HTML5**
- **Pathlib**
- **WebDriverWait**
- **Expected Conditions**
- **Jupyter Notebook**
- **VS Code**
- **Git/GitHub**

| Tecnologia | Utilização |
|---|---|
| `selenium` | Automação e controle do navegador |
| `webdriver` | Inicialização e controle do Google Chrome |
| `WebDriverWait` | Espera explícita por elementos da página |
| `expected_conditions` | Definição das condições necessárias para interação |
| `pathlib` | Localização do arquivo HTML local |
| HTML5 | Página utilizada como sistema de consulta fictício |
| Jupyter Notebook | Desenvolvimento e testes iniciais |
| VS Code | Desenvolvimento do script Python |
| Git/GitHub | Controle de versão e armazenamento do projeto |

---

## Funcionamento

O sistema utilizado no exercício é um arquivo HTML local chamado `consulta_cpf.html`.
O programa utiliza o Selenium para controlar o navegador e realizar a consulta automaticamente.

### Abertura do navegador

A função `abrir_navegador()` inicia o Chrome, maximiza a janela e retorna a instância do navegador:

```python
def abrir_navegador():
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    return navegador
```

### Abertura da página

A função `abrir_pagina()` utiliza `Pathlib` para localizar o arquivo HTML na mesma pasta do script:

```python
def abrir_pagina(navegador):
    caminho_html = Path(__file__).resolve().parent / "consulta_cpf.html"

    if not caminho_html.exists():
        raise FileNotFoundError(f"Arquivo HTML não encontrado: {caminho_html}")
    navegador.get(caminho_html.as_uri())
```

A verificação evita que o programa tente abrir um arquivo inexistente.

### Consulta do CPF

A função `consultar_cpf()` localiza o campo pelo `id`, insere o CPF e depois localiza o botão de consulta:

```python
def consultar_cpf(navegador, cpf):
    campo_cpf = WebDriverWait(navegador, 10).until(EC.presence_of_element_located(("id", "cpf")))
    campo_cpf.send_keys(cpf)

    botao_consultar = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable(("id", "consultar")))
    botao_consultar.click()
```

O CPF utilizado no teste é:

```text
11111111111
```

### Captura do resultado

Após a consulta, o programa aguarda a presença do elemento responsável pelo resultado:

```python
def obter_resultado(navegador):
    resultado = WebDriverWait(navegador, 10).until(EC.presence_of_element_located(("id", "registro")))
    return resultado.text
```

O texto retornado é posteriormente exibido no terminal.

---

## Estrutura do Projeto

```text
Selenium/
│
├── consulta_cpf.html
├── consulta_selenium.py
├── main.ipynb
├── README.md
└── requirements.txt
```

| Arquivo | Descrição |
|---|---|
| `consulta_cpf.html` | Sistema local de consulta utilizado no exercício |
| `consulta_selenium.py` | Programa Python responsável pela automação |
| `main.ipynb` | Notebook utilizado para desenvolvimento e testes |
| `requirements.txt` | Dependências utilizadas no projeto |
| `README.md` | Documentação do projeto |

---

## Configuração

É necessário possuir:

- Python instalado;
- Google Chrome instalado;
- Selenium instalado;
- Arquivo `consulta_cpf.html` na mesma pasta do script;
- Um ambiente Python configurado para executar o projeto.

O Selenium utiliza o Chrome WebDriver para controlar o navegador.
A partir das versões atuais do Selenium, o gerenciamento do driver pode ser realizado automaticamente pelo próprio Selenium Manager.

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/ebrilhantesz/Trilha-TI-Detran.git
```

Acesse a pasta do projeto:

```bash
cd Trilha-TI-Detran
```

Acesse a pasta do exercício:

```bash
cd Selenium
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Ou instale o Selenium diretamente:

```bash
pip install selenium
```

---

## Execução

Execute o programa:

```bash
python consulta_selenium.py
```

O programa irá:

```text
1. Iniciar o Google Chrome
2. Maximizar a janela
3. Localizar o arquivo consulta_cpf.html
4. Abrir o sistema local
5. Localizar o campo CPF
6. Preencher o CPF de teste
7. Localizar o botão Consultar
8. Realizar a consulta
9. Aguardar o resultado
10. Capturar o resultado
11. Exibir o resultado no terminal
12. Encerrar o navegador
```

---

## Fluxo do Programa

```text
                 SCRIPT PYTHON
                       │
                       ▼
                Abrir navegador
                       │
                       ▼
              Abrir consulta_cpf.html
                       │
                       ▼
                 Localizar CPF
                       │
                       ▼
                Preencher CPF
                       │
                       ▼
             Clicar em "Consultar"
                       │
                       ▼
                 WebDriverWait
                       │
                       ▼
              Aguardar resultado
                       │
                       ▼
              Capturar elemento
                       │
                       ▼
                Resultado.text
                       │
                       ▼
                Terminal
                       │
                       ▼
              Fechar navegador
```

---

## Resultado

Durante a execução, o terminal apresenta uma estrutura semelhante a:

```text
==========================
SISTEMA DE CONSULTA DE CPF
==========================

Abrindo sistema de consulta...
Consultando CPF: 11111111111

Resultado da consulta:
--------------------
Nome: Marcelo Manuel
Categoria: B
Situacao: Regular
--------------------
```

O conteúdo exato do resultado depende das informações configuradas no arquivo `consulta_cpf.html`.

Os dados utilizados no exercício são fictícios.

---

## Organização do Código

O `consulta_selenium.py` foi dividido em funções para separar as responsabilidades do programa.

### `abrir_navegador()`

Inicializa o Chrome, maximiza a janela e retorna o navegador.

### `abrir_pagina()`

Localiza o arquivo HTML, verifica sua existência e abre a página no navegador.

### `consultar_cpf()`

Preenche o CPF e realiza a consulta utilizando os elementos da página.

### `obter_resultado()`

Aguarda o resultado aparecer e retorna o texto encontrado.

### `main()`

Coordena todo o fluxo da aplicação.

O navegador é encerrado utilizando `finally`:

```python
try:
    # execução do programa
finally:
    navegador.quit()
```

Dessa forma, o navegador é fechado mesmo caso ocorra algum erro durante a execução.

---

## Repositório

O projeto faz parte do repositório:

**[Trilha-TI-Detran](https://github.com/ebrilhantesz/Trilha-TI-Detran)**

---

## Autor

Desenvolvido por **Eduardo Henrique Brilhante**

---

<p align="center">
  Desenvolvido com Python e Selenium.
</p>
