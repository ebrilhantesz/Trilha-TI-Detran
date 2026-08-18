# Logging no Organizador de Arquivos

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Logging-Automation-4CAF50?style=for-the-badge&logo=python&logoColor=white" alt="Logging">
  <img src="https://img.shields.io/badge/OS-Shutil-3776AB?style=for-the-badge" alt="OS e Shutil">
  <img src="https://img.shields.io/badge/Status-Concluído-2E7D32?style=for-the-badge" alt="Status: Concluído">
</p>

Projeto desenvolvido em Python para transformar um organizador automático de arquivos em um robô capaz de registrar suas operações em um arquivo de log. O programa utiliza `os`, `shutil` e `logging` para organizar arquivos por extensão, registrar movimentações realizadas e tratar possíveis erros sem interromper a execução.

---

## Sumário

- [Sobre o projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Como executar](#como-executar)
- [Exemplo de saída](#exemplo-de-saída)
- [Arquivo de log](#arquivo-de-log)
- [Autor](#autor)

---

## Sobre o projeto

O projeto parte de um organizador automático de arquivos desenvolvido anteriormente, que utiliza `os` e `shutil` para identificar arquivos e separá-los em pastas de acordo com suas extensões.
Nesta etapa, foi adicionada a biblioteca `logging` para criar um diário das operações realizadas pelo programa.
O arquivo `organizacao.log` registra as movimentações com data, hora, nível da mensagem e descrição da operação.

---

## Funcionalidades

- Criação da pasta utilizada para os arquivos de teste.
- Identificação dos arquivos presentes na pasta.
- Identificação da extensão de cada arquivo.
- Criação automática das pastas correspondentes às extensões.
- Movimentação dos arquivos utilizando `shutil.move()`.
- Registro das movimentações realizadas com nível `INFO`.
- Tratamento de erros durante a movimentação dos arquivos.
- Registro de falhas com nível `ERROR`.
- Contagem de arquivos organizados por extensão.
- Geração automática do arquivo `organizacao.log`.
- Leitura e exibição do conteúdo do log no terminal.
- Continuidade da execução mesmo quando ocorre uma falha durante a movimentação.

---

## Tecnologias utilizadas

- **Python 3**
- **os**
- **shutil**
- **logging**
- **collections.Counter**

---

## Estrutura do projeto

```text
Logging/
├── downloads_teste/
│   ├── jpg/
│   ├── pdf/
│   ├── pptx/
│   ├── txt/
│   ├── xlsx/
│   └── zip/
│
├── exemplos/
│   ├── exemplo_logging_vendas.py
│   └── vendas.log
│
├── organizacao.log
└── robo_logging.py
```

### Descrição dos principais arquivos

| Arquivo/Pasta | Descrição |
|---|---|
| `robo_logging.py` | Script principal do organizador com configuração de logging |
| `organizacao.log` | Diário das operações realizadas pelo robô |
| `downloads_teste/` | Pasta utilizada para os arquivos de teste e sua organização |
| `exemplos/` | Arquivos utilizados como referência para o exercício |
| `exemplo_logging_vendas.py` | Exemplo de utilização do módulo `logging` |
| `vendas.log` | Arquivo de log utilizado como referência |

---

## Como executar

### 1. Acesse a pasta do projeto

No terminal, navegue até a pasta `Logging`:

```bash
cd "Logging"
```

### 2. Execute o programa

```bash
python robo_logging.py
```

O programa irá organizar os arquivos da pasta `downloads_teste`, criar as pastas correspondentes às extensões e gerar o arquivo `organizacao.log`.

---

## Exemplo de saída

A execução apresenta no terminal um resumo dos arquivos organizados:

```text
ORGANIZADOR AUTOMÁTICO DE ARQUIVOS

Arquivos organizados:
--------------------------------------------------
jpg/: 1 arquivo(s)
pdf/: 1 arquivo(s)
pptx/: 1 arquivo(s)
txt/: 1 arquivo(s)
xlsx/: 1 arquivo(s)
zip/: 1 arquivo(s)

======================
Organização concluída!
======================
```

Em seguida, o conteúdo do diário é exibido:

```text
Diário da organização:
======================================================================
2026-08-18 09:28:22,342 - INFO - Iniciando a organização dos arquivos
2026-08-18 09:28:22,344 - INFO - Arquivo movido com sucesso: anotacoes.txt -> downloads_teste\txt\anotacoes.txt
2026-08-18 09:28:22,345 - INFO - Arquivo movido com sucesso: apresentacao.pptx -> downloads_teste\pptx\apresentacao.pptx
2026-08-18 09:28:22,348 - INFO - Organização dos arquivos finalizada
```

---

## Arquivo de log

O sistema utiliza a seguinte configuração:

```python
logging.basicConfig(
    filename="organizacao.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)
```

Cada registro contém:

- **Data e hora:** momento em que a operação ocorreu.
- **Nível:** `INFO` para operações realizadas e `ERROR` para falhas.
- **Mensagem:** descrição da operação executada.

Quando um arquivo é movido com sucesso:

```python
logging.info(
    "Arquivo movido com sucesso: %s -> %s",
    arquivo,
    destino
)
```

Quando ocorre uma falha:

```python
logging.error(
    "Falha ao mover o arquivo: %s | Erro: %s",
    arquivo,
    erro
)
```

Dessa forma, o programa mantém um histórico das operações e consegue continuar sua execução mesmo quando um arquivo apresenta algum problema.

---

## Autor

Desenvolvido por **Eduardo Henrique Brilhante**

---

<p align="center">
  Desenvolvido com Python, os, shutil e logging.
</p>
