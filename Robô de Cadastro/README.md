# Robô de Cadastro com Relatório e Dashboard

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=flat&logo=pandas&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-Automation-43B02A?style=flat&logo=selenium&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-4B8BBE?style=flat)
![Looker Studio](https://img.shields.io/badge/Looker%20Studio-Dashboard-4285F4?style=flat&logo=looker&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-2EA44F?style=flat)

Robô desenvolvido em **Python** para automatizar o cadastro de alunos em uma página HTML local, gerar relatórios de sucesso e pendências e disponibilizar os resultados para visualização em um dashboard no **Looker Studio**.

---

## 📋 Sobre o projeto

O projeto executa um fluxo completo de automação:

1. Leitura da base de alunos com Pandas;
2. Abertura de uma página HTML local utilizando Selenium;
3. Cadastro automático dos alunos que possuem WhatsApp;
4. Tratamento de alunos sem WhatsApp;
5. Registro de ocorrências em log;
6. Captura do histórico de inscrições com BeautifulSoup;
7. Geração de relatórios em Excel;
8. Cópia dos relatórios para uma pasta de arquivos processados;
9. Visualização dos resultados em um dashboard no Looker Studio.

A página utilizada é um ambiente de treinamento com dados fictícios. O formulário possui campos de **Nome** e **WhatsApp**, botão de cadastro e uma tabela de histórico identificada por `corpo_tabela`. 

---

## ⚙️ Fluxo do robô

```text
alunos_projeto_final.xlsx
          │
          ▼
     Pandas DataFrame
          │
          ▼
   Verifica WhatsApp
      │          │
      │          └── Vazio
      │                │
      │                ▼
      │          Registra pendência
      │          e usa continue
      │
      └── Preenchido
              │
              ▼
        Selenium + Chrome
              │
              ▼
       Cadastro no HTML
              │
              ▼
      Histórico da página
              │
              ▼
        BeautifulSoup
              │
       ┌──────┴──────┐
       ▼             ▼
    Sucesso       Pendências
       │             │
       └──────┬──────┘
              ▼
        Relatórios Excel
              │
              ▼
         processados/
              │
              ▼
         Looker Studio
```

---

## 📊 Dados de entrada

A planilha `alunos_projeto_final.xlsx` contém as seguintes colunas:

| Campo | Descrição |
|---|---|
| Nome | Nome do aluno |
| CPF | CPF do aluno |
| WhatsApp | Número de WhatsApp |

Um dos registros possui o WhatsApp em branco propositalmente para testar a regra de negócio de pendência.

---

## 🤖 Automação com Selenium

O Selenium inicializa o Chrome e abre o arquivo `index.html` utilizando seu caminho absoluto.

Os campos do formulário são localizados pelos respectivos IDs:

```text
nome
whatsapp
cadastrar
```

O robô preenche os dados e aciona o botão **Cadastrar** para cada aluno que possui WhatsApp.

As interações são protegidas por `try/except`, evitando que uma falha individual interrompa todo o processamento.

---

## 🧠 Regra de negócio

Quando o WhatsApp está vazio:

- O cadastro não é realizado;
- O aluno é registrado no log;
- Nome e CPF são armazenados no relatório de pendências;
- O status da ocorrência é registrado;
- O comando `continue` pula para o próximo aluno.

Quando o WhatsApp está preenchido:

- O nome é inserido no formulário;
- O WhatsApp é inserido no formulário;
- O botão de cadastro é acionado;
- O resultado é registrado no log.

---

## 🔎 Web Scraping com BeautifulSoup

Após o processamento dos alunos, o robô captura o código-fonte atualizado da página através do Selenium.

O histórico de inscrições é localizado pelo:

```html
<tbody id="corpo_tabela">
```

As linhas preenchidas são extraídas e transformadas em uma lista de registros de sucesso.

---

## 📁 Relatórios

Ao finalizar o processamento, são gerados dois arquivos:

```text
relatorio_sucesso_historico.xlsx
relatorio_pendencias.xlsx
```

### Relatório de sucesso

Contém os registros encontrados no histórico da página:

- Nome;
- WhatsApp.

### Relatório de pendências

Contém os alunos que não foram cadastrados:

- Nome;
- CPF;
- Status da ocorrência.

Uma cópia dos dois relatórios é enviada para:

```text
processados/
```

A movimentação dos arquivos também é registrada no log.

---

## 📝 Logging

O robô mantém um diário da execução no arquivo:

```text
robo_cadastro.log
```

São registrados eventos como:

- Início do processamento;
- Quantidade de alunos carregados;
- Abertura da página;
- Cadastros realizados com sucesso;
- Alunos sem WhatsApp;
- Falhas durante o cadastro;
- Captura do histórico;
- Geração dos relatórios;
- Cópia dos relatórios;
- Finalização do processamento.

O formato utilizado contém data, hora, nível e mensagem:

```text
%(asctime)s - %(levelname)s - %(message)s
```

---

## 📊 Dashboard

Os dados do relatório de sucesso podem ser conectados ao **Google Sheets** e posteriormente ao **Looker Studio**.
O dashboard proposto apresenta:

- Total de registros processados;
- Total de cadastros realizados com sucesso;
- Total de pendências;
- Lista dos alunos pendentes em formato de tabela.

Uma forma simples de estruturar os indicadores é:

```text
Total processados = Sucesso + Pendências
```

---

## 🛠️ Tecnologias utilizadas

- **Python** — linguagem principal;
- **Pandas** — leitura, tratamento e exportação dos dados;
- **Selenium WebDriver** — automação do navegador;
- **BeautifulSoup** — extração dos dados do histórico HTML;
- **os** — manipulação de caminhos e diretórios;
- **shutil** — cópia dos relatórios;
- **logging** — registro das etapas e erros;
- **Google Sheets** — disponibilização dos dados para o dashboard;
- **Looker Studio** — visualização dos resultados.

---

## ▶️ Como executar

Instale as dependências:

```bash
pip install pandas openpyxl selenium beautifulsoup4
```

Mantenha os arquivos principais na mesma pasta do script:

```text
Robô de Cadastro/
│
├── alunos_projeto_final.xlsx
├── index.html
├── robo.py
└── README.md
```

Execute:

```bash
python robo.py
```

O Chrome será aberto automaticamente e o robô realizará os cadastros.
Ao final, os relatórios serão gerados e copiados para a pasta `processados`.

---

## 📌 Resultado

O projeto demonstra um fluxo completo de automação e tratamento de dados, combinando:

**Pandas → Selenium → BeautifulSoup → Excel → Looker Studio**

A solução também utiliza estruturas de controle, tratamento de exceções, logging e organização dos arquivos processados.

---

## Autor

Desenvolvido por **Eduardo Henrique Brilhante**

---

<p align="center">
  Desenvolvido com Python, Selenium, BeautifulSoup, Pandas e Looker Studio.
</p>
