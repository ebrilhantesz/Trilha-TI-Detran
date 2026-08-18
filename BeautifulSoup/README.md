# Requests e BeautifulSoup — Raspagem de Dados

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP-2CA5E0?style=flat-square)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-4B8BBE?style=flat-square)
![Web Scraping](https://img.shields.io/badge/Web%20Scraping-Automation-43B02A?style=flat-square)
![Detran PR](https://img.shields.io/badge/Source-Detran%20PR-0E75B6?style=flat-square)
![Status](https://img.shields.io/badge/Status-Concluído-2EA44F?style=flat-square)

Projeto desenvolvido em Python para praticar raspagem básica de dados utilizando as bibliotecas `requests` e `BeautifulSoup`.
O script realiza uma requisição HTTP para o site do Detran-PR, processa o conteúdo HTML retornado e extrai informações específicas da página.

---

## Objetivo

O objetivo deste projeto é praticar os fundamentos de requisições HTTP e análise de documentos HTML com Python, utilizando uma página real como fonte de dados.

## Tecnologias e Ferramentas

- Python
- Requests
- BeautifulSoup
- python-dotenv
- Jupyter Notebook
- Visual Studio Code
- Git
- GitHub

---

## Funcionamento

O projeto executa as seguintes etapas:

1. Configura as variáveis de ambiente relacionadas ao proxy.
2. Define a URL do Detran-PR.
3. Realiza uma requisição `GET` utilizando `requests`.
4. Define um `User-Agent` nos headers da requisição.
5. Verifica o código de status HTTP retornado.
6. Obtém o conteúdo HTML da página.
7. Processa o HTML utilizando `BeautifulSoup`.
8. Localiza e exibe o conteúdo de uma tag `h1`.
9. Localiza e exibe o conteúdo de uma tag `h2`.
10. Localiza um link da página e exibe seu texto e atributo `href`.

## Estrutura do Projeto

```text
BeautifulSoup/
│
├── requests_dados.ipynb
├── requests_dados.py
└── README.md
```

## Exemplo de Saída

```text
Proxy configurado.
200
HTML processado com BeautifulSoup.

Cabeçalho encontrado:
DETRAN/PR/DETRAN/PR

Cabeçalho encontrado:
Navegação principal

Texto:
...
Href:
https://www.parana.pr.gov.br
```

A saída pode variar conforme as alterações realizadas na página do Detran-PR.

---

## Execução

### Jupyter Notebook

Abra o arquivo:

```text
requests_dados.ipynb
```

Execute as células em sequência.

### Python

No terminal, execute:

```bash
python requests_dados.py
```

## Observação

O projeto foi desenvolvido para fins de prática de raspagem de dados com Python. A estrutura e os resultados podem sofrer alterações caso o conteúdo ou a estrutura HTML do site consultado seja modificada.

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
